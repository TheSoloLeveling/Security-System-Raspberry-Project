import React, { useRef, useState, useEffect } from 'react';
import gate from '../data/data1.json'
import camera from '../data/data2.json'
import { BsCurrencyDollar } from 'react-icons/bs';
import { GoPrimitiveDot } from 'react-icons/go';
import { IoIosMore } from 'react-icons/io';
import { DropDownListComponent } from '@syncfusion/ej2-react-dropdowns';
import { GrValidate } from 'react-icons/gr';
import { GiNinjaMask } from 'react-icons/gi';
import { GiIronMask } from 'react-icons/gi';
import { Stacked, Pie, Button, LineChart, SparkLine } from '../components';
import { earningData, medicalproBranding, recentTransactions, weeklyStats, dropdownData, SparklineAreaData, ecomPieChartData } from '../data/dummy';
import { useStateContext } from '../contexts/ContextProvider';
import product9 from '../data/product9.jpg';
import { GiBackup } from "react-icons/gi";

const DropDown = ({ currentMode }) => (
  <div className="w-28 border-1 border-color px-2 py-1 rounded-md">
    <DropDownListComponent id="time" fields={{ text: 'Time', value: 'Id' }} style={{ border: 'none', color: (currentMode === 'Dark') && 'white' }} value="1" dataSource={dropdownData} popupHeight="220px" popupWidth="120px" />
  </div>
);

const Ecommerce = () => {
  const { currentColor, currentMode } = useStateContext();
  const [data, setData] = useState([])
  const { setIsClicked, initialState } = useStateContext();
  const reversedArray = Object.values(gate).reverse();
  const firstFour = reversedArray.slice(0, 4);
 
  async function fetchTableData() {
    
    const URL = "http://127.0.0.1:5000/participant/participants"
    const response = await fetch(URL)

    const participants = await response.json()
    setData(participants)
  }

  async function predict() {
    
    const URL = "http://127.0.0.1:5000/participant/predict"
    const response = await fetch(URL)

    const prediction= await response.json()
    console.log("prediction", prediction)
  }

  async function emptyJSON() {
    console.log("HI")
    const URL = "http://127.0.0.1:5000/participant/deleteData"
    const response = await fetch(URL)

    const participants = await response.json()
    
    console.log(participants)
  }

  useEffect(() => {
    fetchTableData()
    
    
  }, [])

  return (
    <div className="mt-24">
      <div className="flex flex-wrap lg:flex-nowrap justify-center ">
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg h-44 rounded-xl w-full lg:w-80 p-8 pt-9 m-3 bg-hero-pattern bg-no-repeat bg-cover bg-center">
          <div className="flex justify-between items-center">
            <div>
              <p className="font-bold text-gray-400">Total Members</p>
              <p className="text-2xl">{data.length}</p>
            </div>
            <button
              type="button"
              style={{ backgroundColor: currentColor }}
              className="text-2xl opacity-0.9 text-white hover:drop-shadow-xl rounded-full  p-4"
            >
              <GiBackup />
            </button>
          </div>
          <div className="mt-6">
            <Button
              color="white"
              bgColor={currentColor}
              text="Add Member"
              borderRadius="10px"
              
            />
          </div>
        </div>
        <div className="flex m-3 flex-wrap justify-center gap-1 items-center">
          {earningData.map((item) => (
            <div key={item.title} className="bg-white h-44 dark:text-gray-200 dark:bg-secondary-dark-bg md:w-56  p-4 pt-9 rounded-2xl ">
              <button
                type="button"
                style={{ color: item.iconColor, backgroundColor: item.iconBg }}
                className="text-2xl opacity-0.9 rounded-full  p-4 hover:drop-shadow-xl"
              >
                {item.icon}
              </button>
              <p className="mt-3">
                <span className="text-lg font-semibold">{item.amount}</span>
              </p>
              <p className="text-sm text-gray-400  mt-1">{item.title}</p>
            </div>
          ))}
            <div className="mt-6 m-6">
              <Button
                color="white"
                bgColor={currentColor}
                text="Reset"
                borderRadius="10px"
                OnClick={emptyJSON}
                
              />
            </div>
        </div>
      </div>

      <div className="flex gap-10 m-4 pl-28">
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-6 rounded-2xl">
          <div className="flex justify-between items-center gap-2">
            <p className="text-xl font-semibold items-center">Recent Activity</p>
            
          </div>
          <div className="mt-10 w-400 lg:w-400">
            {firstFour.map((item) => (
              <div key={item.timestamp} className="flex justify-between mt-4">
                <div className="flex gap-4">
                  <button
                    type="button"
                    style={{
                      color: "white",
                      backgroundColor: item.gate === "Intruder" ? "red" : "lightgreen",
                    }}
                    className="text-2xl pl-4 pr-4 rounded-lg hover:drop-shadow-xl"
                  >
                    {item.gate === "Intruder" ? (
                        <GiNinjaMask />
                    ) : (<GrValidate />)              
                    }   
                  </button>
                  <div>
                    <p className="text-md font-semibold">{item.gate}</p>
                    <p className="text-sm text-gray-400">captured time : </p>
                    <p className="text-sm text-gray-400">{item.timestamp}</p>
                  </div>
                </div>
                <p className={"text-gray-400"}>
                  {item.gate === "Valid" && <div>No image</div>}
                  {item.gate === "Intruder" && Object.keys(camera).map(key => {
                            const value = camera[key];
                            const [hours, minutes, seconds] = item.timestamp.split(':');
                            const date = new Date();
                            date.setHours(hours);
                            date.setMinutes(minutes);
                            date.setSeconds(seconds); 
                            date.setSeconds(date.getSeconds() + 2);
                            // You can use the key and value to check for a condition
                            const newTimestamp = date.toTimeString().split(' ')[0];
                          
                            console.log(newTimestamp)
                            if (value.timestamp === newTimestamp) {
                              console.log("working")
                              return <img height="100px" width="160px" alt={"name"} src={value.image} />
                            } else {
                              return 
                            }
                        })}
                </p>
              </div>
            ))}
          </div>
          <div className="flex justify-between items-center mt-5 border-t-1 border-color">
            <div className="mt-3 text-gray-400 text-sm">
              4 Recent Transactions
            </div>
          </div>
        </div>
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-6 rounded-2xl w-96 md:w-760">
          <div className="flex justify-between items-center gap-2 mb-10">
            <p className="text-xl font-semibold">Activity Overview</p>
          </div>
          <div className="md:w-full overflow-auto">
            <LineChart />
          </div>
        </div>
      </div>

    </div>
  );
};

export default Ecommerce;
