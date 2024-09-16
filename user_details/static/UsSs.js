const form1=document.querySelector(".detailsform")
// console.log(form1)
form1.addEventListener('submit',event =>{
    event.preventDefault()
    const formData=new FormData(form1)
    console.log(formData.get('user_id'))
    console.log(formData.get('photo'))
    console.log(formData.get('mobile_no'))
    console.log(formData.get('company_id'))
    const data=new URLSearchParams(formData)
    fetch('http://192.168.0.129:5432/user_details',{
        method:'POST',
        body:formData
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
})