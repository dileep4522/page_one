        const form1=document.querySelector(".machform")
// console.log(form1)
form1.addEventListener('submit',event =>{
    event.preventDefault()
    const formData=new FormData(form1)
    console.log(formData.get('machine_id'))
    console.log(formData.get('machine_name'))
    console.log(formData.get('model_no'))
    console.log(formData.get('gateway_id'))
    console.log(formData.get('technical_table'))
    console.log(formData.get('io_group_id'))


    const data=new URLSearchParams(formData)
    // fetch('https://localhost:5432/user_details',{
    //     method:'POST',
//    fetch('http://192.168.0.129:5432/machine_details',{
        method:'POST',
        body:formData
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
})