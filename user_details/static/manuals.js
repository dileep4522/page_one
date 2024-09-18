    const form1 = document.querySelector(".manform")
    // console.log(form1)
    form1.addEventListener('submit',event =>{
    event.preventDefault()
    const formData=new FormData(form1)
    console.log(formData.get('filename'))
    console.log(formData.get('fileurl'))


    // const data=new URLSearchParams(formData)
    fetch('http://127.0.0.1:5000/manuals',{
        method:'POST',
        body:formData
    })
    .then(res => res.json())
    .then(data => console.log(formData))
    .catch(error => console.log(error))
})