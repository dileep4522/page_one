  const form=document.querySelector(".techform")
    // console.log(form1)
    form.addEventListener('submit',event =>{
        event.preventDefault()
        const formData=new FormData(form)
        console.log(formData.get('item_name'))
        console.log(formData.get('manufacture_name'))
        console.log(formData.get('manufacture_model_no'))
        console.log(formData.get('expiry_date'))


//        const formData=new URLSearchParams(formData)
        fetch("http://192.168.0.129:5432/add_technical",{
            method:'POST',
            body:formData
        })
        .then(res => res.json())
        .then(data => console.log(data))
        .catch(error => console.log(error))
    })
