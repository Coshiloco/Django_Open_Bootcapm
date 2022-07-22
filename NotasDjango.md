# Instalacion Django

    ## Instalacion Django en el equipo
        * Instalacion de python
        * Poner en las variables de entorno Python 10
        * Poner en las variables de entorno Python Subcarpeta script
    ## Powershell
        * Poner en el powershell en la carpeta del proyecto python -m pip install Django==4.0.5
    ## Iniciar proyecto de Django
        * Para iniciar el proyecto de Django tenemos que poner el comando django-admin startproject (nombre del proyecto el que nosotros queramos)

# Estructura de archivos dentro de Django

    * En Django podemos tener mas d euna aplicacion por tanto lo que es la aplicacion
        esta contneida dentro de un directorio con el mismo nombre que cuando creamos el proyecto
        con el comando visto arriba
    * el archivo asgi.py y el archivo wsgi.py se encargan de gestionar el servidor que nos
    proporciona Django
    * el archivo settings.py y el archivo urls.py son los dos archivos que vamos
        a gestionar
    * Centrandonos en el archico urls.py este en donde l usuario introduciendo la ulr
        va estar enlazado con las vista o las views que es lo que el usuario
        ve graficamente y que van a estar asociadas a estas dirreciones contenidas a urls.py
        que contendra la vista especifica el entorno grafico que podra ver el usuario
        con esa direccion concreta almacenada en urls.py
    * El archivo settings.py configura el paquete de nuestra aplicacion con django facilitando
        cosas como que ya te viene con diferentes apps o funcionalidades instaladas
        ya sea de seguridad paneles de administracion la configuracion de la base
        de datos teniendo que asi no escribir consultas sql

# Pasos para empezar ha hacer el codigo

    * Hay que posicionarse en la cpartea del pryecto donde se encuentre el archivo manage.py
    * Hay que hacer una migracion de los componentes y archivos del poroyecto al sistema de         permanencia de datos es decir a la base de datos para que haya una cobertura del proyecto y un  backup del mismo y asi se guarde para futuros problemas y siempre al principio y al final
    de cada trabajo en el proyecto se hace con el comando python .\manage.py migrate porque se
    hace cada ejecucion de la aplicacion con el manage.py HAY QUE HACERLO SIEMPRE
    * Lo que hace el comando migrar es generarnos todo el sistema de base
        de datos todos los componentes inicializar el proyecto es decir que tenga
        persistencia que se almacene de forma persistente
    *Cada vez que hagamos una modificacion en el codigo tenemos que ejecutar el comando python .\manage.py migrate para que se actualzicen los datos de forma persistente en la base de datos y DJango pueda funcionar

# Para ejecutar Servidor de pruebas Con Django

    * Una constante para todo es que tenemos que llamar al archivo python .\manage.py
    * Para ejecutar el servidor que nos proporciona DJango y asi visualizar la apgina web que tenemos con el codigo ya MIGRADO es decir ejecutado el comando python .\manage.py migrate
    tenemos que ejecutar el comando python .\manage.py runserver

## Vistas o views.py o Views

    * Lo que vamos a tener dentro de las vistas son diferentes funciones que van a ir enlazadas
        con las rutas del urlpattern que es un array que se enlazara estas funciones de views con las urls contneidas en el array de urlpattern dentro del archivo de urls.py
    * Las views son las que trabajan con los templates o plantillas
        que van a ser los archivos html y css que nosotros vamos ha utilizar para mandarle a la
            views que lo vea el usuario y que esta view se enlaze en la url dentro del archivo urls.py
    * Es decir la view tiene la logica de lo que tiene que hacer la web cuando el usuario entre en al url que le hayamos dicho en el archivo urls.py que este enlazada con esa view esa logica puede ser desde mandar un mensaje estatico a cargar un template o plantilla que sirva para que la vista se la mande a la urls.py y se cargue esa logica en esa url concreta

# Notas del Path de url

    * Cuando estemos escribriendo el path urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/') ] es importante que el path que en nuestro caso es saludo es decir la ruta
    donde vamos a cargar la view con la funcion saludo y la que va a acceder el usuario tiene que terminar la la contrabarra es decir esta / y el siguente parametro es que vista
    queremos que se nor muester por tanto nos vamos al archivo views.FUncion que queremos y que hemos hecho para que ocupe la logica de esa url y como tercer parametro le podemos poner
    el atributo name = "" para luego en el template o plantilla no tener que poner el path
    * from . import views para indicarle que queremos la vista concreta es decir la logica la funcion logica que enlaza con la url de nuestro poryecto por tanto con el . nos situamos en la carpeta en la que estamos y le decimos que nos importe el archivo views para utilizarlo y enlazarlo con la url
    * Para obtener parametros en una url a diferencia de NOdeJS y express que era /:id
    aqui se hace asi publicacionforo/<str:id> / empezando etiqueta html tipo de dato
    el nombre con el que se va a guardar ese parametro en este caso id y cierra de etiqueta html
    a acontnuacion tambien se puede poner otro parametro se peude poner todos los parametros continuos uno detras de otro los parametros de String hay que pasarlo entre comillas por la url
    y donde pone en la url <str:id>  se pasa el parametro asi /"parametroentrecomilla"/
    * %22soyelparametropasadoporurl%22 el %22 representan las comillas sobles en una url
        de http

# Nuevo proyecto nos creamos un nuevo proyecto a que le llamamos plantillas

    * Con el conocido comando de django-admin startproject (nombre del proyecto)
    *Que hacemos al empezar el proyecto siempre migrar el proyecto para generar
        la persistencia de los datos y asi tener la base necesaria
    * La migracion se hacia con el comando python .\manage.py migrate
    * y como en la otra ocasion levantamos el servidor con la instruccion
        python .\manage.py runserver

    * La vista una vez hecho toda la logica es la encargada de devolver el template o plantilla al usuario que es lo que el va ha ver en su pantalla el template o plantilla generalmente van a ser
    archivos html que los cargara la vista para que se puedan imprimir en esa url concreta cerrando asi el circuito conteniendo asi la parte visual lo que separa la parte visual de la logica parte visual plantillas o template parte logica en nuestor archivo de Python con views.py

    * El metodo render que se importa con django.shourcouts import render
    es un metodo que tiene tres parametros
        1. La peticion HTTP que se la pasamos como parametroa a la funcino dentro de views
        2. El nombre de la plantilla que queremos carga en nuestro caso simple.html o la que sea que se encunetre dentro de la carpeta templates y que queramos que vea el usuario, hay que
        especificar la ruta a a partir de la ruta donde le hemos especificado en settings.py en el apartado de TEMPLATES y en el subapartado de DIRS que es un array
        3. El contexto que es lo que queremos que imprima la plantilla o template que va aser un diccionario en Django con una pareja clave-valor

# Uso del contexto en la plantilla o template que va a ejecutar Nuetsra logica en la View

    * Para utilizar una avriable de contexto
    pasada en la url del archivo urls.py en la template o view tenemos que utilizar la sintaxis
    de {{nombre de la variable}}
    * def plantilladinamica(request, name):
    context = {"name": name}
    return render(request=request, template_name='dinamico.html', context=context) ptra cursiosidad es que la logica de la view dinamica alamacena ese nombre pasado en la url en el argumento de la funcion name
    * Las variables pasadas a las templates pueden ser de mucho tipos y si son obejtos {{objetos}}
        podemos acceder a sus metodos mediante el punto dentro del segundo corchete contenido en el primero
    * Podemos pasar mas de un parametro a tarves del context del metodo render creandonos
    el diccionario como el diccionario en python sabemos que el valor de la clave
    puede ser cualquir cosa desde una lista a otro diccionario otro objeto
    podemos psarselo de la siguiente Manera en la logica de Nuestra funcion View

# Bucles y condicionales

    * Para pintar bucles y condicionales dentro de Nuestras templates o plantillas es decir lo que el usuario ve tenemos que utilizar la nomenclatura {% sintaxis bucle for  %} y para cerrar el for {% endfor %} y entere medias ira la impresion de una variable pasada {{variable}} por el parametro context= en el archivo de neustra logica views.py en la funcino asociada a la url y que renderiza nuestra plantilla o template

# Comentarios y filtros

    *Los filtros no es mas que concatenar variables con una extraccion d euna infromación
    se hacen con al tuberia | {{ categories|length }} como se ve en ese ejemplo estamos llamando al array
    categories y le estamos diciendo que en esa variabel de Django nos pinte la longitud de ese array
    *Los comentarios dentro de las plantillas de DJango se hacen primero los de una sola linea :
        1.  {# Esto es un comentario en Django de una sola linea #}
        2. {% comment "Multilinea" %} Esto es un comentario Multilinea en Django {% endcomment %}

# Archivos estaticos

    * EL proposito es implemtar las hojas de estilo CSS y lso archivos que le añaden dinamismo a la pagina como JavaScript
    * Primero tenemos que situarnos en el archivo settings.py
    * Debajo del archivo settings.py tenemos que encontrar donde pone STATIC_URL = 'static/'
    * Debajo de esto tenemos que poner STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static"],
    * Con STATICFILES le estamos indicando que mire en los directorios
    donde vamos a guardar nuestros archivos esticos como CSS y JavaScript como primer parametro que es donde se encuentran
    *El segundo parametro le decimo que nos cargue los archivos y siempre es lo mismo
    * {% load static %} este comando se carga en la plantilla que nos cargara el archivo que nosotros deseemos
    * Posteriormente en esa plantilla hay que poner <link rel="stylesheet" href=" {% static 'style.css' %}" /> donde en el
    href ponemos lo que se va a cargar el archivo en concreto

# Herencia de plantillas

    * Su uso es principalmente ahorrarnos el escribir condigo en lo que
    son los templates que va a renderizar nuestro archivo views.py
    * Aqui dentro de templates tenemos por suppuesto que hacer lo mismo para cargar archivos estaticos
    * En el archivo que nso sirve como base tenemos que poner bloques para que el archivo que herede la plantilla que herede introduzca hay el codigo html que quiera {% block styles %}{% endblock styles %}
    * Para heredar la plantilla  template que va a heredar tenemos que poner este comando al principio {% extends './layouts/base.html' %}
    entre el string el path de donde se ubica el template o plantilla padre y asi cargaremos toda esa plantilla en nuestro template o plantilla hijo

# Bloque de modularizacion 

    * Bien en el bloque de modularizacion lo que hacemos primero es iniciar un proyecto y dentro de ese proyecto 
    nos creamos un modulo con el comando python manage.py startapp (comentarios, nombre del modulo que DJango lo llama APP)
    
# Modelos
    * Los modelos son las clases en Python que repsentan las instancias pero para hacer esto dentro del proyecto tenemos 
    que crear una app que es otro bloque de codigo
    que permite modularizar 
    * Se hace con el comando python manage.py startapp nombre de la app se hace dentro del repositorio donde esta nuestro proyecto
    * Una vez esto nos vamos al archivo models.py donde esta contenida los archivos de nuestra app hacemos la clase
    que nos permite hacer el modelo
    * Para generar el modelo tenemos que ejecutar el comando 
    es python manage.py del projecto de modularizacion makemigrations
    para que nos lo convierta a codigo sql
    * Para geenrar el modelo en la base de datos tenemos que ejecutar el comando python manage.py migrate para que nos lo pase a la base de datos
    python manage.py migrate para hacer la migracion a la base de datos.

# Delegacion de rutas
    *Vemos que el proyecto de django esta compuesto a su vez por apps
    * Estas apps tienen su propio archivo de url.py y un archivo views.py
    * Por lo que se tienen que enlazar con el proyecto principal
    * POr lo que en el archivo de url.py del proyecto tenemos que incluir
    * Esta sentencia path('comments/', include('comentarios.urls'))
    * De donde las rutas van a aprtir todas la raiz comments/ y luego la ruta
    que tengamos en la app en el archivo urls.py donde renderizaremos 
    las vistas que correpondan al path como hemos hecho anterioremente
# Creación y borrado de datos
   *En el archivo de views.py para hacer la prueba nos hemos creado 
   un objeto de python cuyo constructor son los campos de la tabla 
   donde guardaremos los datos
   * En nuestro ejemplo le hemos puesto los campos que hacen falta 
   los que le hemos puesto que puedan ser null podemos no ponerlos 
   pruebacomentario = Coment(name="Bauty", score=100, comment="Bauty es hermoso")
   * La instruccion para que una vez se nos renderize la logica 
   es coger ese objeto y aplicarle la instruccion
   tal como esta en esta linea pruebacomentario.save()
   * Otra forma de crear el objeto directamente es con la instruccion 
   Coment.objects.create(name="Alejandro", comment="Segunda forma de crear el objeto directamente")