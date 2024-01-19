function mensaje(msg,color='green')
    {
      if (color=="success")
      {
        color="green";
      }
      if (color=="error")
      {
        color="red";
      }


      Swal.fire({
        position:"top-end",
        icon: "success",
        title: '¡¡FELICIDADES!!',
        text: msg,
        showConfirmButton: false,
        timer: 1600
    });
  }
    
    