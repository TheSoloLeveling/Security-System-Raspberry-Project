import React, {useState, useEffect} from 'react';
import { GridComponent, Inject, ColumnsDirective, ColumnDirective, Search, Page, row } from '@syncfusion/ej2-react-grids';
import  DataTable, { createTheme } from "react-data-table-component"
import { employeesData, employeesGrid } from '../data/dummy';
import { Header } from '../components';
import { Border } from '@syncfusion/ej2-react-charts';
import {Button} from '../components';
import camera from '../data/data2.json'
import { HiPlay } from 'react-icons/hi';

const Customers = () => {
  const [pending, setPending] = React.useState(true);
  const [rows, setRows] = React.useState([]);
  const [data, setData] = useState([])
  const [perPage, setPerPage] = useState(10)
  const [valueP, setValueP] = useState("waiting for model init ...........")
  const reversedArray = Object.values(camera).reverse();
  const [showAlertValid, setShowAlertValid] = useState(false);
  const [showAlertIntruder, setShowAlertIntruder] = useState(false);
  const [showAlertBasic , setShowAlertBasic ] = useState(true);
 
  const [alertP, setAlertP] = useState("");
  

  async function fetchTableData() {
    setPending(true)
    const URL = "http://127.0.0.1:5000/participant/participants"
    const response = await fetch(URL)

    const participants = await response.json()
    setData(participants)
    setPending(false)
  }

  const loginUser=(image)=>{
    console.log("image", image)
    
    const requestOptions={
        method:"POST",
        headers:{
            'content-type':'application/json'
        },
        body:JSON.stringify(image)
    }
     
    fetch('/participant/predict',requestOptions)
    .then(res=>res.json())
    .then(data=>{
        setShowAlertValid(true);
        setShowAlertBasic(false)
        setAlertP("the person detected is : " + data["predicted label"])
        
        
    })
    .catch(error => {
      setShowAlertIntruder(true)
      setShowAlertBasic(false)
      setAlertP("Not Enough Memory, we are using weak Local machine :(  .Come back later")
      console.error(error);
      
    });

 }

  useEffect(() => {
    fetchTableData()
    
  }, [])
  

  const columns =[
    {
      name: "Image of Intruder",
      cell: row => <div> <p>{row.timestamp}</p>
            <img height="20px" width="300px" alt={"name"} src={row.image} />,
        </div>
    },
    
    {
      name: "Run model",
      cell: row =>
        <button
          type="button"
          style={{ backgroundColor: "green", color: "white",borderRadius: "15px" }}
          className={` text-${48} p-3 w-${12} hover:drop-shadow-xl hover:bg-${"red"}`}
          onClick={() => loginUser(row.image)}
        >
          <HiPlay className='mx-auto'/> Run model
        </button>
    ,
    }
  ]

  const tableCustomStyles= {
    rows: {
        style: {
            minHeight: '50px', // override the row height
        },
    },
    headCells: {
        style: {
            paddingLeft: '8px', // override the cell padding for head cells
            paddingRight: '8px',
            fontSize: '18px',
            fontWeight: 'bold',
            fontFamily:'Palatino',
            justifyContent: 'center',
            borderStyle: 'solid',
				    borderWidth: '1px',
            borderColor: 'rgba(183, 183, 183, 1)'
				    
        },
    },
    cells: {
        style: {
            paddingLeft: '8px', // override the cell padding for data cells
            paddingRight: '8px',
            margin: '8px',
            justifyContent: 'center',
            borderrightStyle: 'solid',
				    borderRightWidth: '3px',
            borderRightColor: 'rgba(183, 183, 183, 1)',
            fontWeight: 'bold',
        },
    },
};

const conditionalRowStyles = [
	{
		when: row => row.gate == "Valid",
		style: {
			backgroundColor: 'rgba(63, 195, 128, 0.9)',
			color: 'white',
			'&:hover': {
				cursor: 'pointer',
			},
		},
	},
	{
		when: row => row.gate == "Intruder",
		style: {
			backgroundColor: 'rgba(242, 38, 19, 0.9)',
			color: 'white',
			'&:hover': {
				cursor: 'pointer',
			},
		},
	},
];



useEffect(() => {
  const timeout = setTimeout(() => {
    setRows(data);
    setPending(false);
  }, 2000);
  return () => clearTimeout(timeout);
}, []);

  return (
    
    <div className='p-6'>

      {showAlertBasic  && (
        <div className="bg-blue-300 text-white p-4 rounded-md">
          {valueP}
        </div>
      )}
      {showAlertIntruder && !showAlertValid && (
        <div className="bg-red-500 text-white p-4 rounded-md">
          {alertP}
        </div>
      )}
      {showAlertValid && !showAlertIntruder && (
        <div className="bg-green-500 text-white p-4 rounded-md">
          {alertP}
        </div>
      )}
      <div>
        <DataTable
          title="All Valid Participants "
          columns={columns}
          data={reversedArray}
          progressPending={pending}
          pagination 
          paginationRowsPerPageOptions={[3]}
          customStyles={tableCustomStyles}
          conditionalRowStyles={conditionalRowStyles}
          />
          
      </div>
    </div>
    
  );
};

export default Customers;
