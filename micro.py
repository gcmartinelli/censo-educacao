import sys
import time
import csv

def console():
        print "Inicializando programa."
        linhas_dict = carregar()
        print """1 - # escolas"""
        while True:
                o = raw_input('Escolha um comando (ex: 1). Digite "q" para sair: \n')
                if o == 'q':
                        break
                if o == '1':
                        resp = {'fed':0,
                                'est':0,
                                'mun':0,
                                'pri':0}
                        for linha in linhas_dict:
                                if linha['ID_DEPENDENCIA_ADM'] == '1':
                                        resp['fed'] += 1
                                elif linha['ID_DEPENDENCIA_ADM'] == '2':
                                        resp['est'] += 1
                                elif linha['ID_DEPENDENCIA_ADM'] == '3':
                                        resp['mun'] += 1
                                elif linha['ID_DEPENDENCIA_ADM'] == '4':
                                        resp['pri'] += 1
                        print """\n\n\nNúmero de escolas: \n
                                Privadas: %s\n
                                Municipais: %s\n
                                Estaduais: %s\n
                                Federais: %s\n""" % (resp['pri'],resp['mun'],
                                                        resp['est'],resp['fed'])

def exportcsv():
        file = csv.writer(open("microdados_csv.csv", "wb"))    

def carregar():
        print "Carregando dados..."
        arq = open('TS_ESCOLA.TXT')
        linhas = arq.readlines()
        linhas_dict = []
        counter = 0
        for linha in linhas:
                counter += 1
                resp_dict = {'ANO_CENSO': linha[1:5],
                                        'PK_COD_ENTIDADE': linha[6:14],
                                        'NO_ENTIDADE': linha[14:114].strip(),
                                        'DESC_SITUACAO_FUNCIONAMENTO': linha[119],
                                        'DESC_SITUACAO_CENSO2012': linha[134],
                                        'DT_ANO_LETIVO_INICIO': linha[137:155],
                                        'DT_ANO_LETIVO_TERMINO': linha[157:175],
                                        'FK_COD_ESTADO': linha[176:178],
                                        'SIGLA': linha[178:180],
                                        'ID_DEPENDENCIA_ADM': linha[198],
                                        'ID_LOCALIZACAO': linha[199],
                                        'DESC_CATEGORIA_ESCOLA_PRIVADA': linha[200],
                                        'ID_CONVENIADA_PP': linha[201],
                                        'ID_TIPO_CONVENIO_PODER_PUBLICO': linha[203],
                                        'ID_MANT_ESCOLA_PRIVADA_EMP': linha[204],
                                        'ID_MANT_ESCOLA_PRIVADA_ONG': linha[205],
                                        'ID_MANT_ESCOLA_PRIVADA_SIND': linha[206],
                                        'ID_MANT_ESCOLA_PRIVADA_SIST_S': linha[207],
                                        'ID_MANT_ESCOLA_PRIVADA_S_FINS': linha[208],
                                        'ID_DOCUMENTO_REGULAMENTACAO': linha[209],
                                        'ID_LOCAL_FUNC_PREDIO_ESCOLAR': linha[210],
                                        'ID_LOCAL_FUNC_SALAS_EMPRESA': linha[211],
                                        'ID_LOCAL_FUNC_PRISIONAL': linha[212],
                                        'ID_LOCAL_FUNC_TEMPLO_IGREJA': linha[213],
                                        'ID_LOCAL_FUNC_CASA_PROFESSOR': linha[214],
                                        'ID_LOCAL_FUNC_GALPAO': linha[215],
                                        'ID_LOCAL_FUNC_OUTROS': linha[216],
                                        'ID_LOCAL_FUNC_SALAS_OUTRA_ESC': linha[217],
                                        'ID_ESCOLA_COMP_PREDIO': linha[218],
                                        'ID_AGUA_FILTRADA': linha[219],
                                        'ID_AGUA_REDE_PUBLICA': linha[220],
                                        'ID_AGUA_POCO_ARTESIANO': linha[221],
                                        'ID_AGUA_CACIMBA': linha[222],
                                        'ID_AGUA_FONTE_RIO': linha[223],
                                        'ID_AGUA_INEXISTENTE': linha[224],
                                        'ID_ENERGIA_REDE_PUBLICA': linha[225],
                                        'ID_ENERGIA_GERADOR': linha[226],
                                        'ID_ENERGIA_OUTROS': linha[227],
                                        'ID_ENERGIA_INEXISTENTE': linha[228],
                                        'ID_ESGOTO_REDE_PUBLICA': linha[229],
                                        'ID_ESGOTO_FOSSA': linha[230],
                                        'ID_ESGOTO_INEXISTENTE': linha[231],
                                        'ID_LIXO_COLETA_PERIODICA': linha[232],
                                        'ID_LIXO_QUEIMA': linha[233],
                                        'ID_LIXO_JOGA_OUTRA_AREA': linha[234],
                                        'ID_LIXO_RECICLA': linha[235],
                                        'ID_LIXO_ENTERRA': linha[236],
                                        'ID_LIXO_OUTROS': linha[237],
                                        'ID_SALA_DIRETORIA': linha[238],
                                        'ID_SALA_PROFESSOR': linha[239],
                                        'ID_LABORATORIO_INFORMATICA': linha[240],
                                        'ID_LABORATORIO_CIENCIAS': linha[241],
                                        'ID_SALA_ATENDIMENTO_ESPECIAL': linha[242],
                                        'ID_QUADRA_ESPORTES_COBERTA': linha[243],
                                        'ID_QUADRA_ESPORTES_DESCOBERTA': linha[244],
                                        'ID_COZINHA': linha[245],
                                        'ID_BIBLIOTECA': linha[246],
                                        'ID_SALA_LEITURA': linha[247],
                                        'ID_PARQUE_INFANTIL': linha[248],
                                        'ID_BERCARIO': linha[249],
                                        'ID_SANITARIO_FORA_PREDIO': linha[250],
                                        'ID_SANITARIO_DENTRO_PREDIO': linha[251],
                                        'ID_SANITARIO_EI': linha[252],
                                        'ID_SANITARIO_PNE': linha[253],
                                        'ID_DEPENDENCIAS_PNE': linha[254],
                                        'ID_SECRETARIA': linha[255],
                                        'ID_BANHEIRO_CHUVEIRO': linha[256],
                                        'ID_REFEITORIO': linha[257],
                                        'ID_DESPENSA': linha[258],
                                        'ID_ALMOXARIFADO': linha[259],
                                        'ID_AUDITORIO': linha[260],
                                        'ID_PATIO_COBERTO': linha[261],
                                        'ID_PATIO_DESCOBERTO': linha[262],
                                        'ID_ALOJAM_ALUNO': linha[263],
                                        'ID_ALOJAM_PROFESSOR': linha[264],
                                        'ID_AREA_VERDE': linha[265],
                                        'ID_LAVANDERIA': linha[266],
                                        'ID_DEPENDENCIAS_OUTRAS': linha[267],
                                        'NUM_SALAS_EXISTENTES': linha[268:273].strip(),
                                        'NUM_SALAS_UTILIZADAS': linha[273:278].strip(),
                                        'ID_EQUIP_TV': linha[278],
                                        'ID_EQUIP_VIDEOCASSETE': linha[279],
                                        'ID_EQUIP_DVD': linha[280],
                                        'D_EQUIP_PARABOLICA': linha[281],
                                        'ID_EQUIP_COPIADORA': linha[282],
                                        'ID_EQUIP_RETRO': linha[283],
                                        'ID_EQUIP_IMPRESSORA': linha[284],
                                        'ID_EQUIP_SOM': linha[285],
                                        'ID_EQUIP_MULTIMIDIA': linha[286],
                                        'ID_EQUIP_FAX': linha[287],
                                        'ID_EQUIP_FOTO': linha[288],
                                        'ID_COMPUTADORES': linha[289],
                                        'NUM_COMPUTADORES': linha[290:295].strip(),
                                        'NUM_COMP_ADMINISTRATIVOS': linha[295:300].strip(),
                                        'NUM_COMP_ALUNOS': linha[300:305].strip(),
                                        'ID_INTERNET': linha[306],
                                        'ID_BANDA_LARGA': linha[307],
                                        'NUM_FUNCIONARIOS': linha[308:313].strip(),
                                        'ID_ALIMENTACAO': linha[313],
                                        'ID_AEE': linha[315],
                                        'ID_MOD_ATIV_COMPLEMENTAR': linha[317],
                                        'ID_MOD_ENS_REGULAR': linha[318],
                                        'ID_REG_INFANTIL_CRECHE': linha[319],
                                        'ID_REG_INFANTIL_PREESCOLA': linha[320],
                                        'ID_REG_FUND_8_ANOS': linha[321],
                                        'ID_REG_FUND_9_ANOS': linha[322],
                                        'ID_REG_MEDIO_MEDIO': linha[323],
                                        'ID_REG_MEDIO_INTEGRADO': linha[324],
                                        'ID_REG_MEDIO_NORMAL': linha[325],
                                        'ID_REG_MEDIO_PROF': linha[326],
                                        'ID_MOD_ENS_ESP': linha[327],
                                        'ID_ESP_INFANTIL_CRECHE': linha[328],
                                        'ID_ESP_INFANTIL_PREESCOLA': linha[329],
                                        'ID_ESP_FUND_8_ANOS': linha[330],
                                        'ID_ESP_FUND_9_ANOS': linha[331],
                                        'ID_ESP_MEDIO_MEDIO': linha[332],
                                        'ID_ESP_MEDIO_INTEGRADO': linha[333],
                                        'ID_ESP_MEDIO_NORMAL': linha[334],
                                        'ID_ESP_MEDIO_PROFISSIONAL': linha[335],
                                        'ID_ESP_EJA_FUNDAMENTAL': linha[336],
                                        'ID_ESP_EJA_MEDIO': linha[337],
                                        'ID_MOD_EJA': linha[338],
                                        'ID_EJA_FUNDAMENTAL': linha[339],
                                        'ID_EJA_MEDIO': linha[340],
                                        'ID_EJA_PROJOVEM': linha[341],
                                        'ID_FUND_CICLOS': linha[342],
                                        'ID_LOCALIZACAO_DIFERENCIADA': linha[343],
                                        'ID_MATERIAL_ESP_NAO_UTILIZA': linha[344],
                                        'ID_MATERIAL_ESP_QUILOMBOLA': linha[345],
                                        'ID_MATERIAL_ESP_INDIGENA': linha[346],
                                        'ID_EDUCACAO_INDIGENA': linha[347],
                                        'ID_LINGUA_INDIGENA': linha[348],
                                        'FK_COD_LINGUA_INDIGENA': linha[349:354],
                                        'ID_LINGUA_PORTUGUESA': linha[354],
                                        'ID_ESPACO_TURMA_PBA': linha[355],
                                        'ID_ABRE_FINAL_SEMANA': linha[356]
                                        }
                linhas_dict += [resp_dict]                    
        print "Banco de dados carregado. %s escolas computadas." % counter
        return linhas_dict