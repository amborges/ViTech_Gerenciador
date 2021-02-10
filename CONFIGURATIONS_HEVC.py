#!/usr/bin/env python3

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
#       Script desenvolvido por Alex Borges, amborges@inf.ufpel.edu.br.        #
#                  Grupo de Pesquisa Video Technology Research Group -- ViTech #
#                                     Universidade Federal de Pelotas -- UFPel #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# script de configuração compatível com o arquivo main.py versão 1.2           #
################################################################################



################################################################################
#                     ARQUIVO DE CONFIGURAÇÃO DEDICADO PARA O                  #
################################################################################
#                                                                              #
#                                                                              #
#                         #   #  #####  #        #  #####                      #
#                         #   #  #       #      #   #                          #
#                         #####  ###      #    #    #                          #
#                         #   #  #         #  #     #                          #
#                         #   #  #####      ##      #####                      #
#                                                                              #
#                                                                              #
################################################################################


 
################################################################################
###                            Configurações Gerais                          ###
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -###
### Aqui tu prepara as condições das simulações que queres executar para os  ###
### teus experimentos. Apesar de estar preparado inicialmente para o HEVC,   ###
### com o software HM, modificações para outros codificadores é relativamente###
### simples. Basicamente é necessário modificar algumas pastas e nomes. Ao   ###
### longo deste arquivo, vou comentando algumas funcionalidades.             ###
################################################################################


#################################
## Ativação de Funcionalidades ##
#################################

#Precisa baixar o HM?
DOWNLOAD = False

#Se precisar que o download do HM seja regredido para alguma versão passada
#então modifique o texto abaixo para a versão requerida. Utilize somente os
#seis primeiros caracteres da versão, por exemplo '16.10+SCM-8.0'
DOWNGRADE_TO = ''

#Precisa compilar o HM?
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

#Lista de QPs a serem utilizados, deixe descomentado o que tu preferir
#Sei que tá CQ_LIST, mas no AV1 é CQ. A ideia é a mesma
#Se quiser utilizar mais valores, é só adicionar
CQ_LIST = [22, 27, 32, 37]


#Parâmetros extras que podem ser incluídos ao codificador. 
#Este é um atributo que permite criar várias simulações onde há apenas a inclusão
#de um ou mais parâmetros ao codificador, além daqueles parâmetros padrões que
#devem estar inclusos (que eu chamo de codificação âncora). Se tu deixar a lista
#vazia, então somente uma única simulação será realizada com aquele vídeo naquele 
#QP. Caso tu adicionar algo, então esse algo será uma simulação a mais que será 
#realizada. Cada nova variação de simulação será identificada nos arquivos de saída.
#POR FAVOR, lembre de adicionar um espaço entre as aspas e o parâmetro em si. Só 
#pra facilitar o meu trabalho durante o código. Sim, foi preguiça.
#Exemplos:
##EXTRA_PARAMS = [] # sem parâmetros extras, 1 conjunto de experimento
##EXTRA_PARAMS = [' --enable-rect-partitions=0'] # UM parâmetro extra, 2 conjuntos de experimentos
##EXTRA_PARAMS = [' --enable-rect-partitions=0', ' --min-partition-size=16 --max-partition-size=64'] # DOIS parâmetros, 3 conjuntos
EXTRA_PARAMS = [' --DisableIntraInInter']



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
CODEC_NAME = 'TAppEncoderStatic'

#tipo de extensão do vídeo. PREFERENCIALMENTE Y4M.
#MAS caso tu preferir utilizar YUV, modifique a função GENERATE_COMMAND
#para incluir as informações de altura, largura, bit-depth, subsample e fps.
VIDEO_EXTENSION = '.yuv'


##########################
## Definição das Pastas ##
##########################

#caminho da pasta de compilação do libaom
#é de lá que ele vai compilar e manter os executáveis
#Caso houver mais de uma versão de libaom, ir adicionando as pastas
# >>>
#>>>  ATENÇÃO: Todas devem estar na mesma pasta atual do projeto!!!!  <<<
# >>>
CODEC_PATHS = ['HM']

#caminhos das pastas dos vídeos separados por resolução
VIDEOS_PATH = {
	'240p': '/home/alex/Videos/objective-2-slow/class_A2/',
	'360p': '/home/alex/Videos/objective-2-slow/class_B/',
	'720p': '/home/alex/Videos/objective-2-slow/class_C2/',
	'1080p': '/home/alex/Videos/objective-2-slow/class_D/',
	'1080pscc': '/home/alex/Videos/objective-2-slow/class_E/',
	'uhd4k': '/home/alex/Videos/objective-2-slow/class_F/'
}

#Lista de vídeos a serem utilizados
#Cada linha é composta por uma resolução (vide acima) e o nome do vídeo
#Também incluí o SI-TI do vídeo, e marquei aqueles que eu considerdo
#recomendados para os nossos experimentos no ViTech.
#Descomente os vídeos que queres utilizar
#Cada linha é composta pelos seguintes elementos
# [ RESOLUÇÃO, NOME DO VÍDEO, LARGURA, ALTURA, SUBAMOSTRAGEM, PROFUNDIDADE DE BITS, NUMERO DE QUADROS ]
VIDEOS_LIST = [
#CLASS_A
#	['240p', 'bqfree_240p_120f',    426, 240, 420, 8, 120], # [124.4, 22.8]
#	['240p', 'bqhighway_240p_120f', 426, 240, 420, 8, 120], # [142.1, 14.3] **
#	['240p', 'bqzoom_240p_120f',    426, 240, 420, 8, 120], # [100.1, 12.3] **
#	['240p', 'chairlift_240p_120f', 426, 240, 420, 8, 64],  # [85.2,   8.2] **
#	['240p', 'dirtbike_240p_120f',  426, 240, 420, 8, 61],  # [72.4,   5.8] **
#	['240p', 'mozzoom_240p_120f',   426, 240, 420, 8, 57],  # [91.6,  33.4] **
	
#CLASS_B
#	['360p', 'blue_sky_360p_120f',           640, 360, 420,  8, 120], # [136.3, 34.2] **
#	['360p', 'controlled_burn_640x360_120f', 640, 360, 420,  8, 120], # [101.2,  3.0]
#	['360p', 'desktop2360p_120f',            640, 360, 420,  8, 120], # [114.5, 10.3]
#	['360p', 'kirland360p_120f',             640, 360, 420,  8, 120], # [ 44.6,  2.3]
#	['360p', 'mmstationary360p_120f',        640, 480, 420,  8, 120], # [ 68.9,  4.2]
#	['360p', 'niklas360p_120f',              640, 360, 420,  8, 120], # [107.8, 11.3]
#	['360p', 'rain2_hdr_amazon_360p',        640, 360, 420, 10,  60], # [ 48.4,  3.0]
#	['360p', 'red_kayak_360p_120f',          640, 360, 420,  8, 120], # [ 72.5, 31.3]
#	['360p', 'riverbed_360p25_120f',         640, 360, 420,  8, 120], # [ 72.8, 30.8]
#	['360p', 'shields2_640x360_120f',        640, 360, 420,  8, 120], # [105.7, 27.5]
#	['360p', 'snow_mnt_640x360_120f',        640, 360, 420,  8, 120], # [140.9,  2.3]
#	['360p', 'speed_bag_640x360_120f',       640, 360, 420,  8, 120], # [ 48.0, 12.6]
#	['360p', 'stockholm_640x360_120f',       640, 360, 420,  8, 120], # [ 91.9, 19.2] **
#	['360p', 'tacomanarrows360p_120f',       640, 360, 420,  8, 120], # [ 78.2,  2.2] **
#	['360p', 'thaloundeskmtg360p_120f',      640, 360, 420,  8, 120], # [169.8,  5.8] **
#	['360p', 'water_hdr_amazon_360p',        640, 360, 420, 10,  60], # [ 30.9,  1.8] **

#CLASS_C
	['720p', 'boat_hdr_amazon_720p',                               1280, 720, 420, 10,  60], # [54.8,  9.2] **
#	['720p', 'dark720p_120f',                                      1280, 720, 420,  8, 120], # [43.3,  6.9]
#	['720p', 'FourPeople_1280x720_60_120f',                        1280, 720, 420,  8, 120], # [80.1,  5.2]
#	['720p', 'gipsrestat720p_120f',                                1280, 720, 420,  8, 120], # [88.1,  5.0]
#	['720p', 'Johnny_1280x720_60_120f',                            1280, 720, 420,  8, 120], # [64.2,  3.9]
	['720p', 'KristenAndSara_1280x720_60_120f',                    1280, 720, 420,  8, 120], # [85.9,  3.9] **
#	['720p', 'Netflix_DinnerScene_1280x720_60fps_8bit_420_120f',   1280, 720, 420,  8, 120], # [18.9,  2.5] **
#	['720p', 'Netflix_DrivingPOV_1280x720_60fps_8bit_420_120f',    1280, 720, 420,  8, 120], # [89.5, 15.2] **
#	['720p', 'Netflix_FoodMarket2_1280x720_60fps_8bit_420_120f',   1280, 720, 420,  8, 120], # [75.1, 28.3] **
#	['720p', 'Netflix_RollerCoaster_1280x720_60fps_8bit_420_120f', 1280, 720, 420,  8, 120], # [56.8, 22.2]
#	['720p', 'Netflix_Tango_1280x720_60fps_8bit_420_120f',         1280, 720, 420,  8, 120], # [52.2, 17.7]
#	['720p', 'rain_hdr_amazon_720p',                               1280, 720, 420, 10,  60], # [62.4,  4.4]
#	['720p', 'vidyo1_720p_60fps_120f',                             1280, 720, 420,  8, 120], # [61.5,  4.4]
#	['720p', 'vidyo3_720p_60fps_120f',                             1280, 720, 420,  8, 120], # [72.1,  7.3]
#	['720p', 'vidyo4_720p_60fps_120f',                             1280, 720, 420,  8, 120], # [61.9,  7.7]

#CLASS_D
#	['1080p', 'aspen_1080p_60f',                                         1920, 1080, 420,  8, 60], # [ 35.0, 11.9]
#	['1080p', 'crowd_run_1080p50_60f',                                   1920, 1080, 420,  8, 60], # [108.2, 25.0] **
#	['1080p', 'ducks_take_off_1080p50_60f',                              1920, 1080, 420,  8, 60], # [ 82.9, 12.5]
#	['1080p', 'guitar_hdr_amazon_1080p',                                 1920, 1080, 420, 10, 60], # [ 22.9,  7.8] **
#	['1080p', 'life_1080p30_60f',                                        1920, 1080, 420,  8, 60], # [ 84.1, 16.9]
#	['1080p', 'Netflix_Aerial_1920x1080_60fps_8bit_420_60f',             1920, 1080, 420,  8, 60], # [ 54.5, 10.3] **
#	['1080p', 'Netflix_Boat_1920x1080_60fps_8bit_420_60f',               1920, 1080, 420,  8, 60], # [ 95.4, 19.9]
#	['1080p', 'Netflix_Crosswalk_1920x1080_60fps_8bit_420_60f',          1920, 1080, 420,  8, 60], # [ 23.1, 15.3]
#	['1080p', 'Netflix_FoodMarket_1920x1080_60fps_8bit_420_60f',         1920, 1080, 420,  8, 60], # [ 39.9, 17.1]
#	['1080p', 'Netflix_PierSeaside_1920x1080_60fps_8bit_420_60f',        1920, 1080, 420,  8, 60], # [ 64.3, 14.8]
#	['1080p', 'Netflix_SquareAndTimelapse_1920x1080_60fps_8bit_420_60f', 1920, 1080, 420,  8, 60], # [ 67.4, 22.1] **
#	['1080p', 'Netflix_TunnelFlag_1920x1080_60fps_8bit_420_60f',         1920, 1080, 420,  8, 60], # [103.2, 60.9] **
#	['1080p', 'old_town_cross_1080p50_60f',                              1920, 1080, 420,  8, 60], # [ 61.1, 11.3]
#	['1080p', 'pan_hdr_amazon_1080p',                                    1920, 1080, 420, 10, 60], # [ 38.5, 11.9]
#	['1080p', 'park_joy_1080p50_60f',                                    1920, 1080, 420,  8, 60], # [103.8, 35.6]
#	['1080p', 'pedestrian_area_1080p25_60f',                             1920, 1080, 420,  8, 60], # [ 36.6, 21.1]
#	['1080p', 'rush_field_cuts_1080p_60f',                               1920, 1080, 420,  8, 60], # [ 93.7, 13.4]
#	['1080p', 'rush_hour_1080p25_60f',                                   1920, 1080, 420,  8, 60], # [ 26.4, 12.0]
#	['1080p', 'seaplane_hdr_amazon_1080p',                               1920, 1080, 420, 10, 60], # [ 52.4, 16.8]
#	['1080p', 'station2_1080p25_60f',                                    1920, 1080, 420,  8, 60], # [ 33.9, 12.9]
#	['1080p', 'touchdown_pass_1080p_60f',                                1920, 1080, 420,  8, 60], # [ 55.7, 11.2]

#CLASS_E
#	['1080pscc', 'CSGO_60f',                1920, 1080, 444, 8, 60], # [ 53.0,  8.5] **
#	['1080pscc', 'DOTA2_60f_420',           1920, 1080, 420, 8, 60], # [ 73.0,  7.8]
#	['1080pscc', 'EuroTruckSimulator2_60f', 1920, 1080, 444, 8, 60], # [ 95.8, 27.7] **
#	['1080pscc', 'Hearthstone_60f',         1920, 1080, 444, 8, 60], # [ 91.2,  4.3]
#	['1080pscc', 'MINECRAFT_60f_420',       1920, 1080, 420, 8, 60], # [ 82.9, 32.0]
#	['1080pscc', 'pvq_slideshow',           1920, 1080, 444, 8, 60], # [185.6,  5.0] **
#	['1080pscc', 'STARCRAFT_60f_420',       1920, 1080, 420, 8, 60], # [ 96.3,  3.3] **
#	['1080pscc', 'wikipedia_420',           1920, 1080, 420, 8, 60], # [170.6, 41.9] **

#CLASS_F
#	['uhd4k', 'Netflix_BarScene_4096x2160_60fps_10bit_420_60f',        4096, 2160, 420, 10, 60], # [14.2,  4.5] **
#	['uhd4k', 'Netflix_BoxingPractice_4096x2160_60fps_10bit_420_60f',  4096, 2160, 420, 10, 60], # [40.7, 19.7] **
#	['uhd4k', 'Netflix_Dancers_4096x2160_60fps_10bit_420_60f',         4096, 2160, 420, 10, 60], # [11.8,  6.7] **
#	['uhd4k', 'Netflix_Narrator_4096x2160_60fps_10bit_420_60f',        4096, 2160, 420, 10, 60], # [22.2,  6.9]
#	['uhd4k', 'Netflix_RitualDance_4096x2160_60fps_10bit_420_60f',     4096, 2160, 420, 10, 60], # [25.3, 17.7] **
#	['uhd4k', 'Netflix_ToddlerFountain_4096x2160_60fps_10bit_420_60f', 4096, 2160, 420, 10, 60], # [51.7, 32.0] **
#	['uhd4k', 'Netflix_WindAndNature_4096x2160_60fps_10bit_420_60f',   4096, 2160, 420, 10, 60], # [42.9,  8.4]
#	['uhd4k', 'street_hdr_amazon_2160p',                               3840, 2160, 420, 10, 60], # [32.5,  5.4]
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
def GENERATE_COMMAND(core, cq, folder, video_path, codec_path, path_id, extra_param, width, height, subsample, bitdepth, num_frames):

	#criando cada parte da linha de comando. Lembrar do espaçamento entre os parâmetros
	
	#comando original que eu usava
	#./TAppEncoderStatic -c encoder_randomaccess_main.cfg -i $(VIDEO) -b hevcbin.h265 -o hevcDecode.yuv -wdt $(WIDTH) -hgt $(HEIGHT) -f $(FTBE) -fr 30 --QP=$(QP) > hevc/hevc.log
	
	#nome da configuração extra_param, se existir
	ep_name = ''
	if extra_param != '':
		ep_name = "_set_" + extra_param.replace(' ', '').replace('-', '').replace('=', '')
	
	#definindo em qual núcleo o experimento será executado
	taskset_param = 'taskset -c ' + core + ' '
	
	#definindo o limite de frames a ser executado
	limit_param = ''
	if(FTBE > 0):
		limit_param = ' -f ' + str(FTBE)
	
	#definindo os valores de informação do vídeo
	video_params = ''
	if(VIDEO_EXTENSION == ".yuv"):
		video_params = ' -wdt ' + str(width) + ' -hgt ' + str(height) + ' -cf ' + str(subsample) + ' --InputBitDepth=' + str(bitdepth) + ' -fr 30'
	
	#definindo a quantização
	#A princípio, se ao invés do QP, for utilizar bitrate, basta trocar a linha para:
	#cq_param = ' --RateControl --TargetBitrate=' + cq
	cq_param = ' --QP=' + cq
	
	#definindo a pasta dos resultados
	this_folder = folder + '/cq_' + cq + '/'
	
	#definindo o arquivo de saída do vídeo codificado
	
	webm_param  = ' -b ' + this_folder + 'video/coded_' + path_id +  ep_name + '.h265'
	webm_param += ' -o ' + this_folder + 'video/coded_' + path_id +  ep_name + '.yuv'
	
	#definindo aonde que ficará salvo as saídas do codificador
	output_filename = this_folder + 'log/out_' + path_id +  ep_name + '.log'
	output_param = ' > ' + output_filename + ' 2>&1'
	
	#definindo outras configurações gerais para o libaom
	fixed_param = ' -c ' + folder + '/../HM/cfg/encoder_randomaccess_main.cfg'
	
	#Criando a linha de comando completa
	codec_command  = taskset_param
	codec_command += codec_path + CODEC_NAME
	codec_command += fixed_param
	codec_command += limit_param
	codec_command += cq_param
	codec_command += video_params
	codec_command += extra_param #normalmente vazio, mas pode conter parâmetros presente em EXTRA_PARAMS
	codec_command += webm_param
	codec_command += ' -i ' + video_path
	codec_command += output_param + ' &'
	#o & comercial no final serve para colocar o processo em segundo plano!
	
	#retornando a linha de comando e o arquivo de saída
	return codec_command, output_filename
	

#A seguinte função lê o arquivo de log e retorna os três valores relevantes de cada arquivo
#entrada, o nome do arquivo que se deseja ler
#saída, o PSNR-Y, o bitrate e o tempo de execução. Todas do tipo float
def get_psnr_bitrate_time(from_file):
	#abro o arquivo obtido do HM
	f = open(from_file)
	#preciso da última linha, mas tenho que passar por todo o arquivo
	#Os dados de bitrate e PSNR estão em algumas linhas antes do final do arquivo
	foundSummary = False
	interesting_line = 0
	
	for lst_line in f:
		if "SUMMARY" in lst_line:
			foundSummary = True
		if foundSummary:
			interesting_line += 1
			#Somente na terceira linha após o summary é que 
			#os dados de bitrate e psnr estão posicionados
			if(interesting_line == 3):
				interesting_line = lst_line
				foundSummary = False
		pass
	f.close()
	
	#Neste momento, eu tenho duas variáveis
	#interesting_line, cujos dados estão como
	#	        5    a    5327.2800   44.2158   47.1400   48.4901   44.8564
	#lst_line, cujos dados estão como
	# Total Time:       51.451 sec.
	
	#O tempo é mais fácil de se pegar.
	#primeiro crio um vetor com o texto
	lst_line = lst_line.split(' ')
	#depois removo elementos vazios desse vetor
	lst_line = list(filter(lambda a: len(a) > 0, lst_line))
	#Agora tenho o vetor abaixo, só me interessa o terceiro elemento
	#['Total', 'Time:', '51.451', 'sec.\n']
	time = float(lst_line[2])
	
	#O bitrate e o PSNR-Y, seguem uma lógica parecida. Separo e depois limpo
	interesting_line = interesting_line.split(' ')
	interesting_line = list(filter(lambda a: len(a) > 0, interesting_line))
	#O vetor abaixo é o que eu obtenho, me interessam os elementos 4 e 5
	#['\t', '5', 'a', '5327.2800', '44.2158', '47.1400', '48.4901', '44.8564', '\n']
	
	psnr_y = float(interesting_line[3])
	bitrate = float(interesting_line[4])
	
	return psnr_y, bitrate, time
	

import os
import urllib.request, urllib.error, urllib.parse
#Função que permite baixar o HM
def DO_DOWNLOAD(codec_path):
	if(os.path.exists(codec_path)):
		#se a pasta já existe, apagar tudo
		os.system('rm -rf ' + codec_path)
	
	#Tenho que pegar a versão daqui, senão dá erro
	#já que não posso atualizar uma variável global
	HM_VERSION = DOWNGRADE_TO
	#Identifica se o usuário deseja uma versão específica
	if HM_VERSION == '':
		#Em caso não quiser, então tenho que procurar a versão mais atualizada do HM
		
		#O caminho geral é sempre o mesmo
		url = 'https://hevc.hhi.fraunhofer.de/svn/svn_HEVCSoftware/tags/'
		
		#Baixo o conteúdo do index.html
		response = urllib.request.urlopen(url)
		webContent = response.read()
		
		#Crio um dicionário vazio para acumular todas as versões
		AllVersions = {}
		
		#Eu separo o conteúdo que me interessa e já removo a parte inicial do código html
		lines = webContent.split(b'<li><a href="')
		
		#Para cada linha das versões...
		for line in lines:
			#Faço um try, pois há linhas no html que não possuem a versão do HM
			try:
				#Aqui terei uma linha como essa: HM-1.0/">HM-1.0/</a></li>
				#Quero pegar somente o texto até o '/', E já aproveito para retirar o 'HM-'
				version = str(line).split('/')[0][5:]
				#Há um problema, a versão 16.20 é superior ao 16.3, mas se eu transformar
				#em float direto, isso não vai ser seguido. Portanto, preciso adicionar
				#um zero entre o ponto e o número, para transformar 16.3 em 16.03
				#Além disso, tenho que remover os '+RExt-1.0/' do número
				version_number = version.split('+')[0]
				integer_part = version_number.split('.')[0]
				decimal_part = version_number.split('.')[1]
				if(len(decimal_part) == 1):
					decimal_part = '0' + decimal_part
				#Aqui, eu junto as partes do número e converto em float
				float_version = float(integer_part + '.' + decimal_part)
				
				#Depois de tudo, eu adiciono as versões no dicionário
				#terei algo assim: '10.1+RExt-2.0': 10.01
				AllVersions.update({version: float_version})
			except:
				#Se der erro no código acima, OK, segue o baile
				continue
				
		
		#Depois de juntar todas as versões, organizo elas em ordem numérica
		AllVersions = dict(sorted(AllVersions.items(), key=lambda item: item[1]))
		
		#Para todos os fins, só me interessa a última versão
		#Já adiciono o HM- que removi anteriormente
		HM_VERSION = 'HM-' + list(AllVersions)[-1]
		
		
	command_line = 'svn checkout https://hevc.hhi.fraunhofer.de/svn/svn_HEVCSoftware/tags/' + HM_VERSION + '/'
	command_line += ' && mv ' + HM_VERSION + ' ' + CODEC_PATHS[0]
	
	#executa a linha de comando
	os.system(command_line)


#Função que compila o HM
#O código já adapta para possíveis versões diferentes de sistema operacional
def DO_COMPILE(os_version, codec_path):
	
	#OBSERVACAO:
	#o codec_path vai incluir uma pasta que não existe, chamada /bin
	#Por isso, sempre coloco um ../ depois de codec_path

	if(os.path.exists(codec_path)):
		#se a pasta já existe, apagar tudo pra deixar uma compilação limpa
		os.system('make -C ' + codec_path + '../build/linux clean')
		os.system('rm -rf ' + codec_path)
	
	#Eu preciso que a pasta /bin exista
	os.system('mkdir ' + codec_path)
	
	#Não sei se faz diferença, atualmente estou testando apenas no Ubuntu 18.04
	make_command = 'make -C ' + codec_path + '../build/linux all'
	
	#if os_version == 18.04:
	#	#Em algumas máquinas, dá pra rodar a linha de baixo. O libaom fica especializado
	#	cmake_command = 'cd ' + codec_path + ' && cmake ..'
	#elif os_version > 18.04:
	#	#Mas na maioria não, daí tem que compilar de forma genérica:
	#	cmake_command = 'cd ' + codec_path + ' && cmake -DAOM_TARGET_CPU=generic ..'
	#else:
	#	#Em caso de ubuntu mais velho, utilizar a seguinte chamada:
	#	cmake_command = 'cd ' + codec_path + ' && cmake -DAOM_TARGET_CPU=generic -DENABLE_DOCS=0 ..'
	
	os.system(make_command)
