function generate_report(){
   var parameters = {
      'action':'search_report',
      'start_date':'2020-06-11',
      'end_date':'2020-06-11',
   }
   $('#data').DataTable({
      responsive: true,
      autoWidth: false,
      destroy: true,
      deferRender: true,
      ajax: {
          url: window.location.pathname,
          type: 'post',
          data: parameters,
          dataSrc: ""
      },
      columnDefs:[
          {
              targets: [-1],
              class: 'text-center',
              orderable: false,
              render: function(data, type, row) {
                 return parseFloat(data).toFixed(2)
              }   
          },
      ],
      initComplete: function(settings, json){
      }
  });

alerta()
}
 
$(function (){
   $('input[name="date_range"]').daterangepicker({
      locale:{
         format: 'YYYY-MM-DD',
         applyLabel: '<i class="fas fa-chart-pie"></i> Aplicar',
         cancelLabel: '<i class="fas fa-times"></i> Cancelar',
      }
   });

   generate_report();
});