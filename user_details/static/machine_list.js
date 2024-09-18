        const form1=document.querySelector(".machineform")
form1.addEventListener('submit',event =>{
    event.preventDefault()
    const formData=new FormData(form1)
    console.log(formData.get('machine_id'))
    console.log(formData.get('kpi_name'))
    console.log(formData.get('datapoints'))
    console.log(formData.get('mode'))
    console.log(formData.get('conversion'))
    console.log(formData.get('x_label'))
    console.log(formData.get('y_label'))
    console.log(formData.get('title'))
    console.log(formData.get('card_type'))
    console.log(formData.get('unit'))


    const data=new URLSearchParams(formData)
    fetch('http://127.0.0.1:5000/machine_list',{
        method:'POST',
        body:data
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
})