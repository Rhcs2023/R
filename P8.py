import streamlit as st
from gtts import gTTS
import tempfile

# Diccionario con palabras a traducir
diccionario = {
    #'a': '1 ',
    #'b': '2 ',
    #'c': '3 ',
    #'d': '4 ',
    #'e': '5 ',
    #'f': '6 ',
    #'g': '7 ',
     'a': 'nuù ',
       'acarrear': 'jíkóñáá ',
       'aceite': 'Dáan ' 'ndutsa ', 
       'adentro': 'inì ',
       'adonde': 'ndéchi ''datyi',
       'agarrar': 'kíhin',
       'agradecido': 'kútahù',
       'ahijada': 'Dáa' ' meñi',
       'ahijado': 'Dáa' ' meñi',
       'ahorrar': 'dakaya',
       'ajo': 'aju ',
       'al': 'ná ',
       'alcanzar': 'kanda ',
       'alegre': 'dee'' ini',
       'alegria': 'aa ',
       'algo': 'joò ',
       'alli': 'uán ',
       'almendra': 'jíva ',
       'alto': 'súkú ', 
       'amargo': 'uhà ',
       'amarillo': 'akuaan ', 
       'amarillo': 'kuáán ',
       'amontonarse': 'tihú',    
       'ancho': 'ajite ',
       'anda': 'jíka ',
       'andar': 'jika ',
       'anochecer': 'akunee ', 
       'año': 'kuià ',
       'año': 'kuià ',
       'aquel': 'uán ', 
       'aqui': 'yáha ',
       'areglar': 'Dáa ' 'vili ', 
       'así': 'Dajan ', 
       'asi': 'suán ', 
       'atras': 'xata ',
       'aullar': 'dakaa yúu ',
       'aunque': 'adua ', 
       'abortar': 'dajoon ',
       'acoiris': 'dikoo ''yáa' ' nkii',
       'aflojar': 'datai ',
       'aguacero': 'dau' 'kánu ',
       'ahorcar': 'dajuéñi ',
       'ahorcar': 'dakuáno ',
       'alla': 'andajan ',
       'alma':'ani ',
       'almohada': 'dáma '' kií '' diki ',
       'alumbrar': 'dakeyée ' ' datnuu',
       'anciana': 'díi' ' tyéun ',
       'anesteciar': 'asixixin ',
       'anillo': 'dáyu ',
       'anotar':'anee ',
       'antiguo': 'ata ',
       'añade': 'datáan ',
       'añadir': 'datáan ',
       'añejo': 'ava ',
       'apenas': 'kani ',
        'arisco': 'dana ',
       'arriba': 'dini ',
       'bañe': 'jichi ',
       'barriga': 'chìi ',
       'bautizar': 'danindusa ',
       'bien': 'kuééni ',
       'bisnieta': 'dáa  ''dukua ' 'dée' ,
       'bisnieto': 'dáa  ''dukua ',
       'blanco': 'akuxi ', 
       'blanco': 'yáá ',
       'bonito': 'luu ',
       'borrego': 'rii ',
       'bravo': 'shraán ',
       'brotar': 'nana',
       'buen': 'tanì ',
       'buenas': 'tanì ', 
       'buenos': 'tanìn ',
       'busque': 'dukuro ',
        'buscaste': 'dukuro ',
       'babajar': 'dakivi ''noo',
       'bajar': 'danuu',
       'bis': 'duka',
       'bien': 'kukueni',
       'bisabuelo': 'ata ''sánu ''siko ',
       'blancura': 'ayaa ' ' vìi ',
       'borrador': 'asndoo ',
       'bramar': 'daníin',
       'bravo': 'dikuée ',

       'cabe': 'aketa ', 
       'cabeza': 'xini ', 
       'cenaste': 'kushini ', #Resoyesta Ku
       'cacahuate': 'déva ''ñúun',
       'cacao': 'síva ',
       'cafe': 'yahá(color) ',
       'cama': 'jito ',
       'cambiar': 'sama ',
       'cambio': 'dandee ', 
       'campra': 'juaro ', 
       'camino': 'ichi ',
       'canasta': 'jika ',
       'canasta': 'jika ',
       'casa': 'vé',#vee
       'cantidad': 'ñáá ',
       'carcel': 'vehe kàa ',
       'creci': 'nijanu ', 
       'ceniza': 'yàà ',
       'chicatana': 'dindoko ', 
       'chiflido': 'dakaduu ',
       'chile': 'yaha ',
       'chivo': 'danisíyu ',
       'choches': 'kuaa ',
       'ciénega': 'ndòhyo', 
       'ciertamente':'andaa' ' kuiti',
       'claro': 'kají ',
       'collar': 'deke',
       'comadre': 'kualiá ',
       'comer': 'kero ',
        'comida': 'deyu ',
       'como': 'ndesa ',
       'compadre': 'mpáà ',
       'comprar': 'kuaan',
       'compra': 'kuaan',
       'compro': 'kuáanná',
       'con': 'jiin',
       'contar': 'dakivi''  kávi ', 
       'contento': 'dee'' ini',
       'contiene': 'ñúhu ',
       'convertirse': 'nduu ',
       'copal': 'deñe ''kutu',
       'cortarse': 'tehndè ',
       'cosa': 'nunkuu ',  
       'costar': 'yaà ',
       'cuando': 'amavi ',
       'cuando': 'nuù ',
       'cuenta': 'dakivi''  kávi ', 
       'cuesta': 'yaà ',
       'cueva': 'túnchi ',
       'culebra': 'koó ', 
       'caca': 'atyatya ',
       'calambre': 'atiyi ',
       'calcetines': 'dámasáa ',
       'caminar': 'dakáá ',
       'caro': 'ávi ',
       'chachalaca': 'daxa ',
       'cielo': 'andeve ',
       'cocer': 'datyiyo ',
       'consumir': 'ayaji ',
       'corazon':'anu ''anima ',
       'correr': 'daya ',
       'culminar': 'dajenekava ',
       'cumbre': 'deke ' ' yuku',
       'decir': 'kéi ',
       'deidad': 'ñuhú ',
       'desde': 'anda ' ,
       'desohojar': 'dakee ',
       'despacio': 'kuéé ',
       'dia': 'dí ', 
       'día': 'dí ', 
       'dias': 'díí ',
       'días': 'díí ',
       'dibujar': 'anatava ',
       'dinero': 'shrúhún ',
       'disgusto': 'aa ',
       'donde': 'ami ',
       'dormir': 'dakidi ', 
       'dedo':'deke'' ndáa',
       'dedo':'dini'' ndáa',
       'defeca':'datyii',
       'defender':'dajana ',
       'deidad':'ane ' 'ñúun',
       'derrumbe':'dée',
       'desaparecer':'dandoo' ' ñúun',
       'desayunar': 'casiinerii ',
       'descomponer':'dakuita',
       'desgranar':'dakoi',
       'despues':'dakuiin',
       'diferente':'diin',
       'diferentes':'diin'' diin',
       'dios':'ane ' 'ñúun',
       'doblar':'dastutna',
       'donde':'demi',
       'echar': 'dakee',
       'egoista': 'jahà ',
       'elefante': 'anda ' ' yuku ',
       'ella': 'an ',
       'empezar': 'kejáhá ',
       'en': 'nuù ', 
       'encontrarse': 'yóó ', 
       'encuentra': 'yóó ', 
       'enloquecer': 'an ' 'sana ',
       'enojarse': 'kiti-iní ',
       'entero': 'níí', 
       'entonceses': 'núsáá ',
       'entrar': 'cháá chuko ',
       'enviar': 'dajn',
       'es': 'kúu ', 
       'esa': 'uán ',
       'escribir': 'cháá ',
       'ese': 'uán ', 
       'espalda': 'xata ',
       'estas': 'kúu ',
       'estan': 'kákuu ',
       'estar': 'yóó ',
       'este': 'yàhá ',
       'él': 'da ',
       'enagua': 'dio ',
       'enfermar': 'dakúu ',
       'engañar': 'dandáu ',
       'engañar':'danávi',
       'enseguida': 'dakuiin ',
       'entenada': 'dáya'' tyáa'' dii ',
       'entenado': 'dáya'' tyáa'' tee ',
       'enterrar': 'danduxin ',
       'entrar': 'dakivi ',
       'entumir': 'asixixin ',
       'escoge': 'dakaxi ',
       'escoger': 'dakaxi ',
       'escondidas': 'dayúu ',
       'escorpion': 'dama '' dnáa ' ,
       'español': 'Dáan ',
       'espiritu': 'ani ',
       'estirar': 'dakaa ',
       'estudiar': 'dajuáan ',
       'excremento': 'atyatya ',
       'empanada': 'staa ''jiti',
       'desayuno': 'casiinirii',
       'facil': 'atuu ' 'yii ',
       'femenino':'síhí',
       'fiesta':'víko', 
       'filoso':'shraán ', 
       'finado':'shraán ', 
       'fuego': 'ñuhú ',
       'fui': ' ',
       'frio': 'avijin ',
       'gente': 'ñagio ',
       'gatear': 'jikandee ',
       'girar': 'dakuiko ',
       'grande': 'kánhu ', 
       'gritar': 'dakaa yúu ',
       'guajolote': 'kóhló ',
       'guajolotito': 'pípí ',
       'garza':'dami ',
       'gemelos': 'dánda ',
        'grande':'anduve ',
       'granizo':'davi ''ñiñi',
       'gastar':'daxi',
       'gavilan':'dían',
       'hace': 'sáhn',
       'hacer': 'sáhn',
       'hablar': 'ka',
       'hable': 'ka',
       'haredar': 'dajañu ',
       'hasta': 'anda ',
       'hay': 'yoo ',#yóó 
       'hermano':'kuàha', 
       'hervir': 'dakiti  ',
       'hervir': 'hervir ',
       'hija': 'dáa',
       'hijastro': 'dáa  ' 'kuu  ''uu  ',
       'hijo': 'dáa  ' ,
       'huipil': 'dikin  ',
       'humo': 'yahà  ',
       'homosexual': 'dínde  ',
       'incierto': 'adi nandaa ', 
       'incierto': 'andaa ',
       'inesperado': 'ama ', 
       'inocente': 'anajini ',
       'inutil': 'anandíii ',
       'ir': 'ki (futuro) ',
       'irse': 'kihín ',
       'hoy': 'avine ',
       'ignora': 'atuu '  '  ini' ,
       'igual': 'danuu',
       'incierto': 'andije ',
       'insomnio': 'atuu '' ñidi',
       'jaguar': 'kuní ',
       'jarro': 'tindohò ',
       'jugar': 'Dadiki ',
       'juguete': 'asiki ',
       'juntar': 'dataka ',
       'la': 'ná ',
       'lago': 'ndòhyo', 
       'lejos': 'jíká ',
       'lengua': 'yaa ',
       'leña': 'ndukú ',
       'lumbre': 'ñuhù',
       'lápiz': 'atee ',
       'lastimar': 'Dajakuee ',
       'leche': 'diku ',
       'leer': 'dakuàan ',
       'levantar': 'danéen ',
       'limpiar': 'davii ',
       'loco': 'dikuée ',
       'lodo': 'ndéyu ',
       'llama': 'nání ',
       'llamarse': 'nání ',
       'llamas': 'náníró ',
       'llamo': 'nání ',
       'llegar': 'chaá',
       'llenar': 'dakutu',
       'lluvia': 'dau ',
       'lluvisna': 'dau ' 'kuetyi',
       'madera': 'yunu ',
       'madre': 'náà ',
       'maguey': 'yáú ',
       'mandar': 'dajn',
       'mano': 'ndaha ',
       'manteca': 'déen ',
       'mayor': 'yukuée ',
       'me': 'ná ',
       'media' 'noche': 'dava ' 'niñu',
       'medio': 'dava ',
       'mentira': 'adio ndije ', 
       'mercado': 'yahu ',
       'mero': 'máá ', 
       'mi': 'ri',
       'mirar': 'koto ', 
       'mismo': 'máá ', 
       'mitad': 'dava ',
       'monte': 'yuko ',
       'mucho': 'anáan ',
       'mucho': 'shraán ',
       'mujer': 'adíi ',
       'musica': 'yàà ',
       'muy': 'shraán ',
       'madrastra': 'díi kiin ',
       'madurar': 'dakutyi ',
       'mala': 'atuu '' ñúun iñi',
       'malo': 'aniváa ',
       'malo': 'atuu '' ñúun iñi',
       'mediano': 'dawa ',
       'mejillas': 'dinuu',
       'memela':'dánde' 'dánsa',
       'mercado': 'ávi ',
       'meter': 'dakíi ',
       'molinillo': 'daka '  ' díva ',
       'mover': 'dakanda ',
       'mueve': 'dakanda ',
       'muro': 'dama ''vée ',
       'nada': 'adana ',
       'nahual': 'akitsi ', 
       'no': 'áan ', 
       'no': 'amiñi ',
       'noche': 'akuaa ', 
       'noche': 'kua ',
       'noches': 'kuaa ',
       'nunca': 'ama  ',
       'nunca': 'avasa ',
       'nacer': 'dakaku ',
       'nada': 'atuu ',
       'nadie': 'ayoo ',
       'nalga': 'data kàa ',
       'negro': 'atuun ',
       'nieta': 'Dáa '' tyáa ' 'dée ',
       'nieto': 'Dáa '' tyáa ' 'dée ',
       'ninguno': 'ayoo ',
       'nuez': 'tiyiki ',
       'nunca': 'dajuexnu ',
       'nariz': 'dijin ',
       'o': 'shí ',
       'odiar': 'koto-uhù ',
       'olla': 'kisi ',
       'olote': 'dañee ',
       'olvidar': 'dakunaa ',
       'orientar': 'Dajáan ',
       'orientar': 'Dajáan ',
       'orilla': 'diin ',
       'otro': 'inga ',
       'padre': 'táà ',
       'pajaro': 'Daa',
       'para': 'ku ',#kúu
       'parados': 'ká-íin',
       'pecho': 'jikà ',
       'pegar': 'kani ',
       'pena': 'aa ',
       'pesos': 'pesos', 
       'petate': 'yuu ',
       'piedra': 'yuú',
       'plato': 'kohò',
       'poner': 'cháá',
       'poseer': 'ñavàha ',
       'posible': 'akuvi ', 
       'probablemente': 'akiva ', 
       'pueblo': 'ñuù ',
       'pajaro'' azul': 'dilaa'' ndii',
       'paloma': 'data ',
       'panteon': 'andaya ',
       'parar': 'dakuiin ',
        'para': 'ja ',
       'pared': 'dama ',
       'párpado': 'dikua ',
       'partir': 'dava ''ndáa',
       'perder': 'dakuita ',
       'perder': 'danduñúun ',
       'perfumado': 'dami ',
       'permiso': 'ayáa ',
       'persona': 'ayivi ',
       'pezon': 'dijin' ' ndika ',
       'pezones': 'deke '' ndika',
       'pide': 'dakan ',
       'pidir': 'dakan ',
       'pierna': 'dánda ',
       'pilon': 'datnu ',
       'piscar': 'dakee ',
       'platano': 'dika ',
       'plaza': 'ávi ',
       'poderoso': 'atu ',
       'polvo': 'ayaka ',
       'por' 'que': 'datyu ',
       'primer': 'dína',
       'primeramente': 'dína',
       'primero': 'dína',
       'pulcera': 'deke '
       'dukun ''ndáa',
       'que': 'ndee ', 
       'queda': 'ndòó',
       'quedarse': 'ndòó',
       'quelite': 'yua',
       'queso': 'dikui ''yuu', 
       'quiere': 'kuní',
       'quitar': 'dakokoo ', 
       'quizá': 'akiva ', 
       'quebrar':'datyi',
       'quien':'andu',
       'regular': 'dawa',
       'rabioso': 'datukuée',
       'rajar': 'datan',
       'rasurar': 'date',
       'rato': 'danyìi',
       'recoger': 'nastútú ',
       'recordar': 'náhá ',
       'regresar': 'yàà ',
       'reir': 'kuako ',
       'relajado': 'kuééni ',
       'repartir': 'tehndè ',
       'repasar': 'dandyíi ',
       'rezar': 'nacuato ',
       'repente': 'ama ', 
       'reunir': 'dataka',
       'rojo': 'akuáa ', 
       'romperse': 'tehndè ',
       'rayo': 'atajia ',
       'registrar':'anee ',
       'repartir':'dajañu ',
       'restar':'dakokoo ',
       'revolver':'daka ',
       'revuelve':'daka ',
       'robar':'dakuína ',
       'romper':'datan ',
       'ropa':'dáma ',
       'rugir':'daníin ',
       'sabroso': 'adin ',
       'salado': 'ada', 
       'salir': 'nana ',
       'se': 'kúu es ser pero  ',
       'seco': 'íchí ',
       'señor':'ihá(divino)',
       'ser': 'kúu ',
       'servilleta': 'dámadita ',
       'si':'ju', 
       'sin':'tuni', 
       'sobrino': 'dajin ', 
       'solamente':'ni',
       'sólido': 'yúú ',
       'sorpresa': 'aa ',
       'su': 'ní ',
       'saborea': 'datee' ' yúu ',
       'salada': 'axe ',
       'saliva': 'dayu ',
       'savia': 'dikui ' 'yutno ',
       'seguida': 'datee ',
       'sembrar': 'dakíi ',
       'sentadera': 'data káa ',
       'silvar': 'dakaduu ',
       'simple': 'atuu   '' diko ',
       'sobrina': 'diku ',
       'soltar': 'daya ',
       'tamal de helote': 'suu ',
       'tambien': 'suni ',
       'tarde': 'ñín ',
       'tarde': 'xañini ',
       'tardes': 'ñíni ', 
       'techo': 'deke ''vée',
       'temprano': 'datsa ',
       'tierra': 'ñuhu ', 
       'tio': 'stoò ', 
       'tirar': 'dakana ',
       'todo': 'níí', 
       'tomar':'koro',
       'tostar': 'dakadu ',
       'trabajo': 'tiun ',
       'trasero': 'shruù ',
       'tu': 'ro', #ró 
       'tela': 'dáma ',
       'terminar': 'dajenekava ',
       'tianguis': 'ávi ',
       'tibio': 'daa ',
       'tirar': 'dajani ',
       'todos': 'diaja  ',
       'tos': 'dayu' ' kaa  ',
       'tortilla': 'staa  ',
       'un': 'in ',
       'una': 'in ',
       'uno': 'in ',
       'usted': 'ní ',
       'va': 'kihín ',
              'valiente': 'daan ',
       'veinte':'okò',
       'vender':'shikó',
       'venir': 'dakivi ''kixi',
       'verdaderamente': 'andaa ' ' kuiti',
       'verde': 'akuii ', 
       'verdura': 'nduà  ',
       'virgen':'ihà(síhí)',
       'volver': 'nduu ',
       'volver':'nduu',
       'voy': 'kihín  ',
       'vueltas': 'jikó ',
       'vacio': 'atuu  ''jañúun ',
       'vestido': 'dio ',
       'viejo': 'ata ',
       'y': 'te ',
       'ya': 'anin ',#ku
       'yo': 'rì ',
       'yerbasanta': 'deva ''ndoo',
       'zurdo': 'dani ',
}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = []
    
    for palabra in palabras:
        if palabra.lower() == 'mi,tu':
            # Si la palabra es 'a', la añadimos al final
            oracion_traducida.append('1 ')
        else:
            oracion_traducida.append(diccionario.get(palabra.lower(), palabra))
    
    # Si hay 'a' en la oración, la movemos al segundo lugar
    if '1 ' in oracion_traducida:
        # Encontramos la posición de '1 ' y la movemos al segundo lugar
        oracion_traducida.remove('1 ')
        oracion_traducida.insert(1, 'ri,ro ')
    
    return " ".join(oracion_traducida)

def reproducir_audio(texto, lang):
    tts = gTTS(text=texto, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
        tts.save(tmp.name)
        with open(tmp.name, 'rb') as audio_file:
            audio_bytes = audio_file.read()
    return audio_bytes

st.title("Traductor de numeros")

# Estado de la sesión para la traducción
if 'oracion_traducida' not in st.session_state:
    st.session_state.oracion_traducida = ""

# Opción para introducir texto
oracion_usuario = st.text_input("Introduce una palabra:")

# Traducir la oración ingresada por el usuario
if oracion_usuario:
    oracion_traducida = traducir_oracion(oracion_usuario)
    st.session_state.oracion_traducida = oracion_traducida
    st.write(f"Traducción: {oracion_traducida}")
    audio_bytes = reproducir_audio(oracion_traducida, 'es')  # Usando español por defecto
    st.audio(audio_bytes, format='audio/mp3')
