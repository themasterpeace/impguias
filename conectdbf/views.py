from django.views.generic import ListView
from .models import DBFTable
from dbfread import DBF

class ListarDatosDBFView(ListView):
    model = DBFTable
    template_name = 'verdatos.html'
    context_object_name = 'registros_dbf'

    def cargar_datos_desde_dbf(self):
        dbf_file_path = 'C:/Users/mesquite/Desktop/dumpsisam/guiashijas.dbf'  # Ruta al archivo DBF
        registros = []

        with DBF(dbf_file_path) as dbf:
            for record in dbf:
                dbf_obj = DBFTable(
                    madre=record['madre'],
                    hija=record['hija'],
                    # Completa otros campos según la estructura de tu tabla DBF
                )
                registros.append(dbf_obj)

        return registros

    def get_queryset(self):
        return self.cargar_datos_desde_dbf()

