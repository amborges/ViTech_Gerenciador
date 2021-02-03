#!/usr/bin/env python3

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
#       Script desenvolvido por Alex Borges, amborges@inf.ufpel.edu.br.        #
#                  Grupo de Pesquisa Video Technology Research Group -- ViTech #
#                                     Universidade Federal de Pelotas -- UFPel #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# script de configuração compatível com o arquivo main.py versão 1.1           #
################################################################################



################################################################################
#                     ARQUIVO DE CONFIGURAÇÃO DEDICADO PARA O                  #
################################################################################
#                                                                              #
#                                                                              #
#                          #####  #       #    ##                              #
#                          #   #   #     #   #  #                              #
#                          #####    #   #       #                              #
#                          #   #     # #        #                              #
#                          #   #      #         #                              #
#                                                                              #
#                                                                              #
################################################################################


 
################################################################################
###                            Configurações Gerais                          ###
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -###
### Aqui tu prepara as condições das simulações que queres executar para os  ###
### teus experimentos. Apesar de estar preparado inicialmente para o AV1,    ###
### com o software libaom, modificações para outros codificadores é          ###
### relativamente simples. Basicamente é necessário modificar algumas pastas ###
### e nomes. Ao longo deste arquivo, vou comentando algumas funcionalidades. ###
################################################################################


#################################
## Ativação de Funcionalidades ##
#################################

#Precisa baixar o libaom?
DOWNLOAD = False

#Se precisar que o download do libaom seja regredido para alguma versão passada
#então modifique o texto abaixo para a versão requerida. Utilize somente os
#seis primeiros caracteres da versão, por exemplo 'df1c60'
DOWNGRADE_TO = ''

#Precisa compilar o libaom?
COMPILE  = False

#Quer realizar somente uma única simulação, para ver alguma coisa específica?
TESTE    = False

#É para executar de fato o experimento, com todas as simulações possíveis?
EXECUTE  = True

#Quer que mostre na tela o estado geral das simulações?
#Caso opte por False, o arquivo de log ainda será gerado.
VERBOSE = True

######################################
## Parâmetros Gerais das Simulações ##
######################################

#Lista de núcleos que podem ser utilizados, lembre sempre de deixar pelo menos
#um único núcleo para o sistema operacional.
ALLOWED_CORES = [0, 1, 2]

#Lista de CQs a serem utilizados, deixe descomentado o que tu preferir
CQ_LIST = [20, 32, 43, 55] #short list
#CQ_LIST = [20, 24, 28, 32, 36, 39, 43, 47, 51, 55] #full list

#Parâmetros extras que podem ser incluídos ao codificador. 
#Este é um atributo que permite criar várias simulações onde há apenas a inclusão
#de um ou mais parâmetros ao codificador, além daqueles parâmetros padrões que
#devem estar inclusos (que eu chamo de codificação âncora). Se tu deixar a lista
#vazia, então somente uma única simulação será realizada com aquele vídeo naquele 
#CQ. Caso tu adicionar algo, então esse algo será uma simulação a mais que será 
#realizada. Cada nova variação de simulação será identificada nos arquivos de saída.
#POR FAVOR, lembre de adicionar um espaço entre as aspas e o parâmetro em si. Só 
#pra facilitar o meu trabalho durante o código. Sim, foi preguiça.
#Exemplos:
##EXTRA_PARAMS = [] # sem parâmetros extras, 1 conjunto de experimento
##EXTRA_PARAMS = [' --enable-rect-partitions=0'] # UM parâmetro extra, 2 conjuntos de experimentos
##EXTRA_PARAMS = [' --enable-rect-partitions=0', ' --min-partition-size=16 --max-partition-size=64'] # DOIS parâmetros, 3 conjuntos
EXTRA_PARAMS = []



############################
## Configuração do SCRIPT ##
############################

#Quantidade de quadros a ser executado (frames to be executed)
#Se deixar com valor negativo, então o vídeo inteiro será codificado
FTBE = 5

#tempo de espera para verificar os processos em pilha (em segundos)
#Quanto mais curto, mais vezes ele faz uma leitura dos processos
#em um mesmo período de tempo. Tente ser razoável, por exemplo, 
#tu vai executar somente vídeos UHD4K, sabe-se que eles levam pelo
#menos uns três dias (chegando a sete em alguns casos) para codificar.
#Neste caso, não faz o menor sentido verificar o processo a cada 30seg.
#Para esse caso específico, uma vez por dia tá bom (86400). Agora
#se tu vai usar o setup completo de vídeos, uma vez a cada uma hora 
#tá de bom tamanho (3600)
WAITING_TIME = 30

#Número máximo de núcleos que podem ser utilizados simultaneamente
#Em geral, se tu selecionou os cores disponíveis, é pq eles podem
#ser utilizados. Acaso tiveres alguma restrição, modificar aqui.
#O detalhe é que o computador não utilizará todos os núcleos
#anotados em ALLOWED_CORES
MAX_CORES = len(ALLOWED_CORES)

#nome do codificador. Se houver alguma mudança, mude aqui
CODEC_NAME = 'aomenc'

#tipo de extensão do vídeo. PREFERENCIALMENTE Y4M.
#MAS caso tu preferir utilizar YUV, modifique a função GENERATE_COMMAND
#para incluir as informações de altura, largura, bit-depth, subsample e fps.
VIDEO_EXTENSION = '.y4m'


##########################
## Definição das Pastas ##
##########################


#caminho da pasta de compilação do libaom
#o /bin/ no final é criado automaticamente pelo script.
#é de lá que ele vai compilar e manter os executáveis
CODEC_PATH = '/home/alex/Documents/MAKEFILE_AS_PYTHON/aom/bin/'

#caminhos das pastas dos vídeos separados por resolução
VIDEOS_PATH = {
	'240p': '/home/alex/Videos/objective-2-slow/class_A/',
	'360p': '/home/alex/Videos/objective-2-slow/class_B/',
	'720p': '/home/alex/Videos/objective-2-slow/class_C/',
	'1080p': '/home/alex/Videos/objective-2-slow/class_D/',
	'1080pscc': '/home/alex/Videos/objective-2-slow/class_E/',
	'uhd4k': '/home/alex/Videos/objective-2-slow/class_F/'
}

#Lista de vídeos a serem utilizados
#Cada linha é composta por uma resolução (vide acima) e o nome do vídeo
#Também incluí o SI-TI do vídeo, e marquei aqueles que eu considerdo
#recomendados para os nossos experimentos no ViTech.
#Descomente os vídeos que queres utilizar
VIDEOS_LIST = [
#CLASS_A
#	['240p', 'bqfree_240p_120f'],    # [124.4, 22.8]
	['240p', 'bqhighway_240p_120f'], # [142.1, 14.3] **
	['240p', 'bqzoom_240p_120f'],    # [100.1, 12.3] **
	['240p', 'chairlift_240p_120f'], # [85.2, 8.2]   **
#	['240p', 'dirtbike_240p_120f'],  # [72.4, 5.8]   **
#	['240p', 'mozzoom_240p_120f'],   # [91.6, 33.4]  **
	
#CLASS_B
#	['360p', 'blue_sky_360p_120f'],           # [136.3, 34.2] **
#	['360p', 'controlled_burn_640x360_120f'], # [101.2, 3.0]
#	['360p', 'desktop2360p_120f'],            # [114.5, 10.3]
#	['360p', 'kirland360p_120f'],             # [44.6, 2.3]
#	['360p', 'mmstationary360p_120f'],        # [68.9, 4.2]
#	['360p', 'niklas360p_120f'],              # [107.8, 11.3]
#	['360p', 'rain2_hdr_amazon_360p'],        # [48.4, 3.0]
#	['360p', 'red_kayak_360p_120f'],          # [72.5, 31.3]
#	['360p', 'riverbed_360p25_120f'],         # [72.8, 30.8]
#	['360p', 'shields2_640x360_120f'],        # [105.7, 27.5]
#	['360p', 'snow_mnt_640x360_120f'],        # [140.9, 2.3]
#	['360p', 'speed_bag_640x360_120f'],       # [48.0, 12.6]
#	['360p', 'stockholm_640x360_120f'],       # [91.9, 19.2]  **
#	['360p', 'tacomanarrows360p_120f'],       # [78.2, 2.2]   **
#	['360p', 'thaloundeskmtg360p_120f'],      # [169.8, 5.8]  **
#	['360p', 'water_hdr_amazon_360p'],        # [30.9, 1.8]   **

#CLASS_C
#	['720p', 'boat_hdr_amazon_720p'],                               # [54.8, 9.2]  **
#	['720p', 'dark720p_120f'],                                      # [43.3, 6.9]
#	['720p', 'FourPeople_1280x720_60_120f'],                        # [80.1, 5.2]
#	['720p', 'gipsrestat720p_120f'],                                # [88.1, 5.0]
#	['720p', 'Johnny_1280x720_60_120f'],                            # [64.2, 3.9]
#	['720p', 'KristenAndSara_1280x720_60_120f'],                    # [85.9, 3.9]  **
#	['720p', 'Netflix_DinnerScene_1280x720_60fps_8bit_420_120f'],   # [18.9, 2.5]  **
#	['720p', 'Netflix_DrivingPOV_1280x720_60fps_8bit_420_120f'],    # [89.5, 15.2] **
#	['720p', 'Netflix_FoodMarket2_1280x720_60fps_8bit_420_120f'],   # [75.1, 28.3] **
#	['720p', 'Netflix_RollerCoaster_1280x720_60fps_8bit_420_120f'], # [56.8, 22.2]
#	['720p', 'Netflix_Tango_1280x720_60fps_8bit_420_120f'],         # [52.2, 17.7]
#	['720p', 'rain_hdr_amazon_720p'],                               # [62.4, 4.4]
#	['720p', 'vidyo1_720p_60fps_120f'],                             # [61.5, 4.4]
#	['720p', 'vidyo3_720p_60fps_120f'],                             # [72.1, 7.3]
#	['720p', 'vidyo4_720p_60fps_120f'],                             # [61.9, 7.7]

#CLASS_D
#	['1080p', 'aspen_1080p_60f'],                                         # [35.0, 11.9]
#	['1080p', 'crowd_run_1080p50_60f'],                                   # [108.2, 25.0] **
#	['1080p', 'ducks_take_off_1080p50_60f'],                              # [82.9, 12.5]
#	['1080p', 'guitar_hdr_amazon_1080p'],                                 # [22.9, 7.8]   **
#	['1080p', 'life_1080p30_60f'],                                        # [84.1, 16.9]
#	['1080p', 'Netflix_Aerial_1920x1080_60fps_8bit_420_60f'],             # [54.5, 10.3]  **
#	['1080p', 'Netflix_Boat_1920x1080_60fps_8bit_420_60f'],               # [95.4, 19.9]
#	['1080p', 'Netflix_Crosswalk_1920x1080_60fps_8bit_420_60f'],          # [23.1, 15.3]
#	['1080p', 'Netflix_FoodMarket_1920x1080_60fps_8bit_420_60f'],         # [39.9, 17.1]
#	['1080p', 'Netflix_PierSeaside_1920x1080_60fps_8bit_420_60f'],        # [64.3, 14.8]
#	['1080p', 'Netflix_SquareAndTimelapse_1920x1080_60fps_8bit_420_60f'], # [67.4, 22.1]  **
#	['1080p', 'Netflix_TunnelFlag_1920x1080_60fps_8bit_420_60f'],         # [103.2, 60.9] **
#	['1080p', 'old_town_cross_1080p50_60f'],                              # [61.1, 11.3]
#	['1080p', 'pan_hdr_amazon_1080p'],                                    # [38.5, 11.9]
#	['1080p', 'park_joy_1080p50_60f'],                                    # [103.8, 35.6]
#	['1080p', 'pedestrian_area_1080p25_60f'],                             # [36.6, 21.1]
#	['1080p', 'rush_field_cuts_1080p_60f'],                               # [93.7, 13.4]
#	['1080p', 'rush_hour_1080p25_60f'],                                   # [26.4, 12.0]
#	['1080p', 'seaplane_hdr_amazon_1080p'],                               # [52.4, 16.8]
#	['1080p', 'station2_1080p25_60f'],                                    # [33.9, 12.9]
#	['1080p', 'touchdown_pass_1080p_60f'],                                # [55.7, 11.2]

#CLASS_E
#	['1080pscc', 'CSGO_60f'],                # [53.0, 8.5]   **
#	['1080pscc', 'DOTA2_60f_420'],           # [73.0, 7.8]
#	['1080pscc', 'EuroTruckSimulator2_60f'], # [95.8, 27.7]  **
#	['1080pscc', 'Hearthstone_60f'],         # [91.2, 4.3]
#	['1080pscc', 'MINECRAFT_60f_420'],       # [82.9, 32.0]
#	['1080pscc', 'pvq_slideshow'],           # [185.6, 5.0]  **
#	['1080pscc', 'STARCRAFT_60f_420'],       # [96.3, 3.3]   **
#	['1080pscc', 'wikipedia_420'],           # [170.6, 41.9] **

#CLASS_F
#	['uhd4k', 'Netflix_BarScene_4096x2160_60fps_10bit_420_60f'],        # [14.2, 4.5]  **
#	['uhd4k', 'Netflix_BoxingPractice_4096x2160_60fps_10bit_420_60f'],  # [40.7, 19.7] **
#	['uhd4k', 'Netflix_Dancers_4096x2160_60fps_10bit_420_60f'],         # [11.8, 6.7]  **
#	['uhd4k', 'Netflix_Narrator_4096x2160_60fps_10bit_420_60f'],        # [22.2, 6.9]
#	['uhd4k', 'Netflix_RitualDance_4096x2160_60fps_10bit_420_60f'],     # [25.3, 17.7] **
#	['uhd4k', 'Netflix_ToddlerFountain_4096x2160_60fps_10bit_420_60f'], # [51.7, 32.0] **
#	['uhd4k', 'Netflix_WindAndNature_4096x2160_60fps_10bit_420_60f'],   # [42.9, 8.4]
#	['uhd4k', 'street_hdr_amazon_2160p'],                               # [32.5, 5.4]
]



############################# [ [ [ A  T  E  N  Ç  Ã  O ] ] ] ########################################
#       Aqui se encontram funções que poderão sofrer mudanças. Deve-se alterar o que for preciso     #
#           para que a linha de comando seja adequada ao codificador que se está utilizando          #
######################################################################################################

#entradas vindas da classe LIST_OF_EXPERIMENTS, esses valores não são alteráveis.
#todos os valores são do tipo texto.
#   core, número do núcleo em que o experimento vai ser executado
#   cq, valor de quantização (CQ)
#   folder, nome da pasta em que o experimento será executado
#   video_path, caminho completo do vídeo que será codificado
def GENERATE_COMMAND(core, cq, folder, video_path, extra_param = ''):

	#criando cada parte da linha de comando. Lembrar do espaçamento entre os parâmetros
	
	#nome da configuração extra_param, se existir
	ep_name = ''
	if extra_param != '':
		ep_name = "_set_" + extra_param.replace(' ', '').replace('-', '').replace('=', '')
	
	#definindo aonde a codificação será executada
	cd_param = 'cd ' + folder + ' & '
	
	#definindo em qual núcleo o experimento será executado
	taskset_param = 'taskset -c ' + core + ' '
	
	#definindo o limite de frames a ser executado
	limit_param = ''
	if(FTBE > 0):
		limit_param = ' --limit=' + str(FTBE)
	
	#definindo a quantização
	#A princípio, se ao invés do CQ, for utilizar bitrate, basta trocar a linha para:
	#cq_param = ' --end-usage=vbr --target-bitrate=' + cq
	cq_param = ' --end-usage=q --cq-level=' + cq
	
	#definindo o arquivo de saída do vídeo codificado
	webm_param = ' -o '+ folder +'/cq_' + cq + '/webm/coded' +  ep_name + '.webm'
	
	#definindo aonde que ficará salvo as saídas do codificador
	output_filename = folder + '/cq_' + cq + '/log/out' +  ep_name + '.log'
	output_param = ' > ' + output_filename + ' 2>&1'
	
	#definindo outras configurações gerais para o libaom
	fixed_param = ' --verbose --psnr --frame-parallel=0 --tile-columns=0 --passes=2 --cpu-used=0 --threads=1 --kf-min-dist=1000 --kf-max-dist=1000 --lag-in-frames=19'
	
	#Criando a linha de comando completa
	codec_command  = cd_param
	codec_command += taskset_param
	codec_command += CODEC_PATH + CODEC_NAME
	codec_command += fixed_param
	codec_command += limit_param
	codec_command += cq_param
	codec_command += extra_param #normalmente vazio, mas pode conter parâmetros presente em EXTRA_PARAMS
	codec_command += webm_param
	codec_command += ' ' + video_path
	codec_command += output_param + ' &'
	#o & comercial no final serve para colocar o processo em segundo plano!
	
	#retornando a linha de comando e o arquivo de saída
	return codec_command, output_filename
	

#A seguinte função lê o arquivo de log e retorna os três valores relevantes de cada arquivo
#entrada, o nome do arquivo que se deseja ler
#saída, o PSNR-Y, o bitrate e o tempo de execução. Todas do tipo float
def get_psnr_bitrate_time(from_file):
	#abro o arquivo obtido do libaom
	f = open(from_file)
	#preciso da última linha, mas tenho que passar por todo o arquivo
	for lst_line in f:
		pass
	f.close()
	#separo a linha em palavras
	words = lst_line.split(' ')
	#removo os indexes que não contêm palavras
	words = list(filter(lambda a: len(a) > 0, words))
	#idx = o que aparece
	#0  =  Stream
	#1  =  0
	#2  =  PSNR
	#3  =  (Overall/Avg/Y/U/V)
	#4  =  44.452
	#5  =  45.206
	#6  =  44.286
	#7  =  48.271
	#8  =  48.832
	#9  =  4193982
	#10  =  bps
	#11  =  27382
	#12  =  ms\n
	
	#O que me interessa são o PSNR-Y (6), bitrate (9) e o tempo (11)
	psnr_y = float(words[6])
	bitrate = float(words[9])
	time = float(words[11])
	return psnr_y, bitrate, time
	

import os
#Função que permite baixar o libaom
#pego somente o caminho do aom, sem o bin/
def DO_DOWNLOAD():
	codec_path = CODEC_PATH[:-4]
	if(os.path.exists(codec_path)):
		#se a pasta já existe, apagar tudo
		os.system('rm -rf ' + codec_path)
	
	#faz download do libaom e coloca na pasta desejada
	git_command = 'git clone https://aomedia.googlesource.com/aom ' + codec_path
	
	#caso deseja fazer downgrade...
	if DOWNGRADE_TO != '':
		git_command += ' && cd ' + codec_path + ' && git reset --hard ' + DOWNGRADE_TO
	
	#executa o git
	os.system(git_command)


#Função que compila o libaom
#O código já adapta para possíveis versões diferentes de sistema operacional
def DO_COMPILE(os_version):
	#se precisar compilar o libaom, então COMPILA
	if(os.path.exists(CODEC_PATH)):
		#se a pasta já existe, apagar tudo pra deixar uma compilação limpa
		os.system('rm -rf ' + CODEC_PATH)
	os.system('mkdir ' + CODEC_PATH)
	
	if os_version == 18.04:
		#Em algumas máquinas, dá pra rodar a linha de baixo. O libaom fica especializado
		cmake_command = 'cd ' + CODEC_PATH + ' && cmake ..'
	elif os_version > 18.04:
		#Mas na maioria não, daí tem que compilar de forma genérica:
		cmake_command = 'cd ' + CODEC_PATH + ' && cmake -DAOM_TARGET_CPU=generic ..'
	else:
		#Em caso de ubuntu mais velho, utilizar a seguinte chamada:
		cmake_command = 'cd ' + CODEC_PATH + ' && cmake -DAOM_TARGET_CPU=generic -DENABLE_DOCS=0 ..'
	make_command = 'cd ' + CODEC_PATH + ' && make'
	os.system(cmake_command)
	os.system(make_command)
