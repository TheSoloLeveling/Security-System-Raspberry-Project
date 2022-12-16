import React, { useState, useRef, useEffect } from 'react';
import { Player } from 'video-react';


const Scheduler = () => {
  const videoRef = useRef(null)
  const photoRef = useRef(null)

  const [hasPhoto, setHasPhoto] = useState(false)

  const getVideo = () => {
    navigator.mediaDevices.getUserMedia({ video: {width: 800, height: 600}})
    .then(stream => {
      let video = videoRef.current
      video.srcObject = stream
      video.play()
    })
    .catch(err => {
      console.error(err)
    })
  }

  useEffect(() => {
    getVideo()
  }, [videoRef])

  return (
    <div className="flex ml-28 mt-10">

      <object type="text/html" data="http://10.202.43.144:4747/" width="800px" height="600px" >
        </object>
    
    </div>
  );
};

export default Scheduler;
