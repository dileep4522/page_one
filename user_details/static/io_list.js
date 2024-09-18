    const form1=document.querySelector(".ioform")
    form1.addEventListener('submit',event =>{
    event.preventDefault()
    const formData=new FormData(form1)
    console.log(formData.get('io_group'))
    console.log(formData.get('io_type'))
    console.log(formData.get('io_name'))
    console.log(formData.get('io_value'))
    console.log(formData.get('io_color'))
    console.log(formData.get('io_range'))
    console.log(formData.get('io_unit'))
    console.log(formData.get('control'))
    console.log(formData.get('alarm'))



    const data=new URLSearchParams(formData)
    fetch('http://127.0.0.1:5000/io_list',{
        method:'POST',
        body:data
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
})