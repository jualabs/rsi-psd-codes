import cherrypy
from clima import climaNaEstrada

class ServidorWeb(object):
    
    header = "<html><head></head><body>Descrubra o clima entre duas cidades <br>"
    footer = "</body></html>"
    form = """<form method="get" action="clima">
              Origem: <input type="text" value="" name="origem" /><br><br>
              Destino: <input type="text" value="" name="destino" /><br><br>
              <button type="submit">Descubra!</button>
            </form>"""
          
    @cherrypy.expose
    def index(self):
        return self.header+self.form+self.footer
    
    @cherrypy.expose
    def clima(self, origem, destino):
        clima = climaNaEstrada(origem,destino)
        listaCidades = clima.resolve()
        keys = sorted(clima.resolve())
        
        result = """<table>
                        <tr>
                            <td>Localizacao</td>
                            <td>Temperatura</td>
                            <td>Umidade</td> 
                        </tr>"""
        
        for key in keys:
            cidade = key[1][0]
            estado = key[1][1]
            pais = key[1][2]
            temperatura = listaCidades[key][0]
            umidade = listaCidades[key][1]
            result += """<tr>
                            <td>"""+cidade+","+estado+","+pais+"""</td>
                            <td>"""+str(temperatura)+"""</td> 
                            <td>"""+str(umidade)+"""</td>
                        </tr>"""
        
        result += "</table>"
        
        return self.header+self.form+result+self.footer

if __name__ == '__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(ServidorWeb())