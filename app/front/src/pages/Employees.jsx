import React, {useState, useEffect} from 'react';
import { GridComponent, Inject, ColumnsDirective, ColumnDirective, Search, Page, row } from '@syncfusion/ej2-react-grids';
import  DataTable, { createTheme } from "react-data-table-component"
import { employeesData, employeesGrid } from '../data/dummy';
import { Header } from '../components';
import data from '../pages/data.json' 
import { Border } from '@syncfusion/ej2-react-charts';


const Employees = () => {
  
  const [pending, setPending] = React.useState(true);
  const [rows, setRows] = React.useState([]);
  const [perPage, setPerPage] = useState(10)

  const columns =[
    {
      name: "Status",
      selector: (row) => row.gate
    },
    {
      name: "Password",
      selector: (row) => row.password
    },
    {
      name: "Time",
      selector: (row) => row.timestamp
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
            justifyContent: 'center',
            fontFamily:'Palatino',
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
          title="Recordings of the gate keypad"
          columns={columns}
          data={data}
          progressPending={pending}
          pagination
          customStyles={tableCustomStyles}
          conditionalRowStyles={conditionalRowStyles}
          />
          
      </div>
    </div>
    
  );
};
export default Employees;
