# Pw2-Lab04
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>
<div align="center">
    <span style="font-weight:bold;"><h2>INFORME DE LABORATORIO</h2></span>
</div>

<div style="text-align:center">
<table>
<theader>
    <tr><th colspan="6" style="width:50%; height:auto; text-align:center">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td colspan="5">Laboratorio de Programación Web 2</td>
    </tr>
    <tr>
        <td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td>
    </tr>
    <tr>
        <td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td colspan="2">FECHA DE PRESENTACIÓN:</td><td>05-Jun-2022</td><td colspan="2">HORA DE PRESENTACIÓN:</td><td>16:00</td>
    </tr>
    <tr>
        <td colspan="3">INTEGRANTES:
        <ol>
        <li>Blanco Trujillo, Antony Jacob</li>
        <li>Cahuana Aguilar, Josué Mathías Miguel</li>
        <li>Hancco Velásquez, Jessica Geraldine</li>
        <li>Mayta Nolasco, Oliver Alessandro</li>
        <li>Umasi Cariapaza, Carlos Daniel</li>
        </ol>
        </td>
        <td colspan="2"> NOTA:</td>
        <td><!--Espacio para la calificación de práctica-->     </td>
    </tr>
    <tr>
        <td colspan="6">DOCENTE:<br>
        Mg. Richart Smith Escobedo Quispe
        </td>
    </tr>
</tdbody>
</table>
</div>

<table>
    <theader>
        <tr>
            <th style="text-align:center">SOLUCIÓN Y RESULTADOS</th>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td>
            I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS<br>
            </td>
        </tr>
        <tr>
            <td>
            II. SOLUCIÓN DEL CUESTIONARIO<br>
            <br>
            &nbsp;<b>¿Qué son los archivos *.pyc?</b><br>
            Los archivos con extención .pyc son las versiones que contienen código de bytes compilados de archivos .py, lo que facilita el tiempo de ejecución en la interpretación de un programa en lenguaje Python. Un archivo .pyc siempre tiene su archivo .py del cuál tendrá la compilación guardada para posteriores invocaciones.<br> 
            <br>&nbsp;<b>¿Para qué sirve el directorio pycache?</b><br>
            El directorio _pycache_ es creado automaticamente al importar un módulo por 1° vez en archivos .py que sean ejecutados, este directorio es creado a la par (mismo nivel) de los archivos .py y en el contiene la version .pyc de los archivos .py. Tambien se puede compilar manualmente un módulo para que se guarde en el directorio _pycache_, ejecutando:
            <br><code>&nbsp;&nbsp;&nbsp;>>>import py_compile<br>
            &nbsp;&nbsp;&nbsp;>>> py_compile.compile('modulo.py') </code><br>
            ó, para todo un directorio que contenga archivos .py para compilar
            <br><code>&nbsp;&nbsp;&nbsp;python -m compileall</code><br>
            <br>&nbsp;<b>¿Cuáles son los usos y lo que representa el subguión en Python?</b><br>
            El subguión o guión bajo es un caracter especial en Python y se usa en casos como:
            <ul>
                <li>Internacionalización (i18n) o Localización (l10n)
                <li>Para almacenar el valor de la última expresión en intérprete
                <li>Al separar los dígitos de un número
                <li>Para ignorar valores específicos
                <li>Distintos significados especiales al nombre de variables o funciones(para la inicialización y funciones de clase)
            </ul>
            <br>
            </td>
        </tr>
        <tr>
            <td>
            III. CONCLUSIONES<br>
                <ul>
                    <li>Las estructuras contenedoras de python son muy similares, pero se diferencian por el manejo(funciones de llamado, eliminación y agregación) y tipo(variables de igual o de diferentes tipos de datos) de elemento que pueden almacenar.</li>
                    <li>Pygame es un módulo (librería) de Python que facilita la creación de juegos y programas multimedia.</li>
                    <li>Las clases en Python funcionan con el mismo mecanismo del Paradigma de POO (Programación Orientada a Objetos) con atributos, médtodos y propiedades (atributos) de herencia que se pueden usar. Además que, al igual que en otros lenguajes, con las clases se pueden crear diferentes tipos de datos, y con los objetos se pueden crear instancias de esos tipos de datos. </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<table>
    <theader>
        <tr>
            <th style="text-align:center">RETROALIMENTACIÓN GENERAL</th>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td>
            <!--Espacio para la retroalimentación dada por el docente-->
            </td>
        </tr>
    </tbody>
</table>

<table>
    <theader>
        <tr>
            <th style="text-align:center">REFERENCIAS Y BIBLIOGRAFÍA</th>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td>
                [1] Escobedo, R., 2022. pw2/labs/lab04 at main · rescobedoq/pw2. [online] GitHub. Available at: https://github.com/rescobedoq/pw2/tree/main/labs/lab01.<br>
                [2] ¿Cómo creo un archivo .pyc?. Programming FAQ 3.10... - Manual multilingüe - OULUB, 2021. Available at: https://www.oulub.com/es-ES/Python/faq.programming-how-do-i-create-a-pyc-file.
            </td>
        </tr>
    </tbody>
</table>
