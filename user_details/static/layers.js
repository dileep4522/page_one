const form1=document.querySelector(".layerform")
// console.log(form1)
form1.addEventListener('submit',event =>{
    event.preventDefault()
    const formData=new FormData(form1)
    console.log(formData.get('layer_type'))
    console.log(formData.get('layer_name'))
    console.log(formData.get('company_logo'))
    console.log(formData.get('location'))


    const data=new URLSearchParams(formData)
    // fetch('https://localhost:5432/user_details',{
    //     method:'POST',
    fetch('http://192.168.0.129:5432/layers',{
        method:'POST',
        body:data
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
})