       const form1=document.querySelector(".cardform")
// console.log(form1)
form1.addEventListener('submit',event =>{
    event.preventDefault()
    const formData=new FormData(form1)
    console.log(formData.get('card_type'))


    const data=new URLSearchParams(formData)
    fetch('http://127.0.0.1:5000/cards',{
        method:'POST',
        body:data
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
})