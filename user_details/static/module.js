        const form1=document.querySelector(".moduleform")
// console.log(form1)
form1.addEventListener('submit',event =>{
    event.preventDefault()
    const formData=new FormData(form1)
    console.log(formData.get('module_name'))
    console.log(formData.get('icons'))
    console.log(formData.get('type'))



    // const data=new URLSearchParams(formData)
    fetch('http://127.0.0.1:5000/modules',{
        method:'POST',
        body:formData
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
})

