from flask import Flask, render_template, Response, abort, send_from_directory
from datetime import date

app = Flask(__name__)
BASE = "https://serviciosdigitales.evoluciono.net"

SERVICIOS = [
 {"slug":"actas-registro-civil","nombre":"Actas del Registro Civil","icono":"📄","descripcion":"Orientación y apoyo para consultar y obtener actas de nacimiento, matrimonio y defunción."},
 {"slug":"curp","nombre":"Consulta de CURP","icono":"🪪","descripcion":"Asistencia para consultar, descargar y revisar tu Clave Única de Registro de Población."},
 {"slug":"constancia-situacion-fiscal","nombre":"Constancia de Situación Fiscal","icono":"🧾","descripcion":"Asesoría para consultar y obtener tu Constancia de Situación Fiscal mediante los canales oficiales del SAT."},
 {"slug":"numero-seguridad-social","nombre":"Número de Seguridad Social","icono":"🏥","descripcion":"Orientación para localizar o consultar tu NSS a través de los servicios oficiales del IMSS."},
 {"slug":"constancia-no-inhabilitacion","nombre":"Constancia de No Inhabilitación","icono":"💼","descripcion":"Apoyo para identificar requisitos y gestionar solicitudes de constancias laborales según la autoridad competente."},
 {"slug":"recibos-cfe","nombre":"Consulta de recibos CFE","icono":"💡","descripcion":"Asistencia para consultar y descargar recibos de energía eléctrica mediante canales autorizados."},
 {"slug":"redaccion-oficios-solicitudes","nombre":"Redacción de oficios y solicitudes","icono":"📝","descripcion":"Elaboramos oficios, solicitudes, cartas formales y escritos dirigidos a instituciones, escuelas, empresas y particulares."},
 {"slug":"elaboracion-documentos","nombre":"Elaboración de documentos","icono":"📑","descripcion":"Redacción, captura, edición y formato de documentos personales, administrativos y comerciales, según tus necesidades."},
 {"slug":"contratos-compraventa-terrenos","nombre":"Contratos de compraventa","icono":"✍️","descripcion":"Apoyo en la preparación de contratos de compraventa de terrenos y orientación sobre su revisión legal."}
]

@app.route("/")
def inicio():
    return render_template("index.html", servicios=SERVICIOS, base=BASE)

@app.route("/servicios/<slug>")
def servicio(slug):
    item = next((s for s in SERVICIOS if s["slug"] == slug), None)
    if not item:
        abort(404)
    return render_template("servicio.html", servicio=item, base=BASE)

@app.route("/privacidad")
def privacidad():
    return render_template("privacidad.html", base=BASE)

@app.route("/googlea08e544e8054840b.html")
def google_verification():
    return send_from_directory("verification", "googlea08e544e8054840b.html", mimetype="text/html")

@app.route("/robots.txt")
def robots():
    return Response(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", mimetype="text/plain")

@app.route("/sitemap.xml")
def sitemap():
    paths = ["/", "/privacidad"] + ["/servicios/" + s["slug"] for s in SERVICIOS]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{BASE}{p}</loc></url>" for p in paths) + "</urlset>"
    return Response(xml, mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)
