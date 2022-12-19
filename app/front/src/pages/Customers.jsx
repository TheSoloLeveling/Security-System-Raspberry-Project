import React, {useState, useEffect} from 'react';
import { GridComponent, Inject, ColumnsDirective, ColumnDirective, Search, Page, row } from '@syncfusion/ej2-react-grids';
import  DataTable, { createTheme } from "react-data-table-component"
import { employeesData, employeesGrid } from '../data/dummy';
import { Header } from '../components';
import data from '../pages/data.json' 
import { Border } from '@syncfusion/ej2-react-charts';

const Customers = () => {
  const [pending, setPending] = React.useState(true);
  const [rows, setRows] = React.useState([]);
  const [data, setData] = useState([])
  const [perPage, setPerPage] = useState(10)

  async function fetchTableData() {
    setPending(true)
    const URL = "http://127.0.0.1:5000/participant/participants"
    const response = await fetch(URL)

    const participants = await response.json()
    setData(participants)
    setPending(false)
  }

  useEffect(() => {
    fetchTableData()
  }, [])
  

  const columns =[
    {
      name: "Full Name",
      selector: (row) => row.title
    },
    {
      name: "Designation",
      selector: (row) => row.description
    },
    {
      name: "Image Profil",
      cell: row => <img height="100px" width="56px" alt={"name"} src={row.photo} />,
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
      <div>
        <DataTable
          title="All Valid Participants "
          columns={columns}
          data={data}
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
