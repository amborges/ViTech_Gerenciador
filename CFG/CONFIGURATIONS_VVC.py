#!/usr/bin/env python3

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
#       Script desenvolvido por Alex Borges, amborges@inf.ufpel.edu.br.        #
#                  Grupo de Pesquisa Video Technology Research Group -- ViTech #
#                                     Universidade Federal de Pelotas -- UFPel #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# script de configuração compatível com o arquivo main.py versão 1.3           #
################################################################################



################################################################################
#                     ARQUIVO DE CONFIGURAÇÃO DEDICADO PARA O                  #
################################################################################
#                                                                              #
#                                                                              #
#                         #        # #        #  #####                         #
#                          #      #   #      #   #                             #
#                           #    #     #    #    #                             #
#                            #  #       #  #     #                             #
#                             ##         ##      #####                         #
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

#Precisa baixar o VTM?
DOWNLOAD = True

#Se precisar que o download do HM seja regredido para alguma versão passada
#então modifique o texto abaixo para a versão requerida. Utilize somente os
#seis primeiros caracteres da versão, por exemplo '274e8f'
DOWNGRADE_TO = '274e8f'

#Precisa compilar o VTM?
COMPILE  = True

#Quer realizar somente uma única simulação, para ver alguma coisa específica?
TESTE    = False

#É para executar de fato o experimento, com todas as simulações possíveis?
EXECUTE  = True

#Quer que mostre na tela o estado geral das simulações?
#Caso opte por False, o arquivo de log ainda será gerado.
VERBOSE = False

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
EXTRA_PARAMS = []



############################
## Configuração do SCRIPT ##
############################

#Quantidade de quadros a ser executado (frames to be executed)
#Se deixar com valor negativo, então o vídeo inteiro será codificado
FTBE = 3

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
CODEC_NAME = 'EncoderAppStatic'

#tipo de extensão do vídeo. PREFERENCIALMENTE Y4M.
#MAS caso tu preferir utilizar YUV, modifique a função GENERATE_COMMAND
#para incluir as informações de altura, largura, bit-depth, subsample e fps.
VIDEO_EXTENSION = '.yuv'


##########################
## Definição das Pastas ##
##########################

#caminho da pasta de compilação do VTM
#é de lá que ele vai compilar e manter os executáveis
#Caso houver mais de uma versão de VTM, ir adicionando as pastas
# >>>
#>>>  ATENÇÃO: Todas devem estar na mesma pasta atual do projeto!!!!  <<<
# >>>
CODEC_PATHS = ['VTM']


############################# [ [ [ A  T  E  N  Ç  Ã  O ] ] ] ########################################
#       Aqui se encontram funções que poderão sofrer mudanças. Deve-se alterar o que for preciso     #
#           para que a linha de comando seja adequada ao codificador que se está utilizando          #
######################################################################################################

#entradas vindas da classe LIST_OF_EXPERIMENTS, esses valores não são alteráveis.
#todos os valores são do tipo texto.
#   core, número do núcleo em que o experimento vai ser executado
#   cq, valor de quantização (CQ ou QP)
#   folder, nome da pasta em que o experimento será executado
#   video_path, caminho completo do vídeo que será codificado
#   codec_path, caminho para o executável
#   home_path, caminho da pasta atual em que o script está executando
#   path_id, nome do executável
#   extra_param, parâmetros extras de execução, caso houver
#   width, largura do vídeo
#   height, altura do vídeo
#   subsample, subamostragem (444, 422, 420 etc)
#   bitdepth, profundidade de bits (esperado 8 ou 10)
#   num_frames, número de quadros que há no vídeo
#   frames_per_unit, número de frames por unidade de tempo do vídeo
#   unit_size, tamanho da unidade de tempo do vídeo em segundos
def GENERATE_COMMAND(core, cq, folder, video_path, codec_path, home_path, path_id, extra_param, width, height, subsample, bitdepth, num_frames, frames_per_unit, unit_size):
	#criando cada parte da linha de comando. Lembrar do espaçamento entre os parâmetros
	
	#comando completo
	#EncoderAppStatic -c encoder_randomaccess_vtm.cfg --Verbosity=4 -wdt {WDT} -hgt {HGT} --FrameRate={FPS} --QP={CQP} --BitstreamFile=coded_{VIDEO}.vvc --InputFile={VIDEO}.yuv --InputBitDepth={BD} --OutputBitDepth={BD} --InternalBitDepth={BD} 
	#SE subamostragem 444: -cf {SUB}
	
	#nome da configuração extra_param, se existir
	ep_name = ''
	if extra_param != '':
		ep_name = "_set_" + extra_param.replace(' ', '').replace('-', '').replace('=', '')
	
	#definindo a pasta da saída dos resultados
	this_folder = home_path + '/' + folder + '/cq_' + cq + '/'
	
	#PARÂMETROS
	
	#definindo em qual núcleo o experimento será executado
	taskset_param = 'taskset -c ' + core + ' '
	
	#definindo o caminho e nome do executável: ./EncoderAppStatic
	executable_param = codec_path + CODEC_NAME
	
	#definindo o arquivo de configuração principal: -c encoder_randomaccess_main.cfg
	main_cfg_param = ' -c ' + home_path + '/VTM/cfg/encoder_randomaccess_vtm.cfg'
		
	#Caso vídeo tiver subamostragem 444
	if (subsample == 444):
		main_cfg_param += ' -cf ' + str(subsample)
		
	#definindo as informações do vídeo
	video_param  = ' -wdt ' + str(width) #width
	video_param += ' -hgt ' + str(height) #hight
	video_param += ' --FrameRate={:.2f}'.format(float(frames_per_unit) / float(unit_size)) #fps
	video_param += ' --InputBitDepth=' + str(bitdepth) #bit depth
	video_param += ' --OutputBitDepth=' + str(bitdepth) #bit depth
	video_param += ' --InternalBitDepth=' + str(bitdepth) #bit depth
	
	#definindo o nível de quantização
	quant_param  = ' --QP=' + str(cq)
	
	#definindo o limite de frames a ser executado
	limit_param = ' -f ' + str(num_frames)
	
	#Condições especiais de configuração do limite de quadros
	#Caso o usuário limitar algum valor, usar esse valor
	if(FTBE > 0):
		limit_param = ' -f ' + str(FTBE)
		
	#definindo o caminho que será salvo o arquivo de vídeo codificado
	codfile_param = ' --BitstreamFile=' + this_folder + 'video/coded_' + path_id +  ep_name + '.vvc'
	
	#definindo o caminho do vídeo de entrada
	rawvideo_param = ' --InputFile=' + video_path

	#definindo o caminho do arquivo de log e o comando para forçar saída nesse arquivo
	output_filename = this_folder + 'log/out_' + path_id +  ep_name + '.log'
	logfile_param = ' --Verbosity=4 > ' + output_filename + ' 2>&1'
	
		
	#O HEVC Gera um arquivo extra, vamos definir aonde ele ficará
	#para possibilitar remover ele depois
	toremove = this_folder + 'video/coded_' + path_id +  ep_name + '.yuv'
	toremove_param  = ' --ReconFile=' + toremove
	
	remove_params_files = ' && rm -f ' + toremove
	
	#Criando a linha de comando completa
	codec_command  = taskset_param 
	codec_command += executable_param 
	codec_command += main_cfg_param 
	codec_command += video_param 
	codec_command += quant_param 
	codec_command += limit_param 
	codec_command += codfile_param 
	codec_command += rawvideo_param 
	codec_command += toremove_param 
	codec_command += logfile_param
	
	codec_command += remove_params_files
	
	#o & comercial no final serve para colocar o processo em segundo plano!
	codec_command += ' &'
	
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
		if "Total Frames" in lst_line:
			foundSummary = True
		if foundSummary:
			interesting_line += 1
			#Somente a segunda linha após o "Total Frames" é que 
			#os dados de bitrate e psnr estão posicionados
			if(interesting_line == 2):
				interesting_line = lst_line
				foundSummary = False
	f.close()
	
	#Neste momento, eu tenho duas variáveis
	#interesting_line, cujos dados estão como
	#5    a    2738.2080   43.2481   43.8931   45.5898   43.3501
	#lst_line, cujos dados estão como
	# Total Time:       30.291 sec. [user]       30.294 sec. [elapsed]
	
	#O tempo é mais fácil de se pegar.
	#primeiro crio um vetor com o texto
	lst_line = lst_line.split(' ')
	#depois removo elementos vazios desse vetor
	lst_line = list(filter(lambda a: len(a) > 0, lst_line))
	#Agora tenho o vetor abaixo, só me interessa o terceiro elemento
	#     ['Total', 'Time:', 30.291, 'sec.', '[user]', 30.294, 'sec.', '[elapsed]']
	#idx:    0         1       2       3        4         5      6          7
	time = float(lst_line[2])
	
	#O bitrate e o PSNR-Y, seguem uma lógica parecida. Separo e depois limpo
	interesting_line = interesting_line.split(' ')
	interesting_line = list(filter(lambda a: len(a) > 0, interesting_line))
	#O vetor abaixo é o que eu obtenho, me interessam os elementos 4 e 5
	#     ['\t', '5', 'a', '2738.2080', '43.2481', '43.8931', '45.5898', '43.3501', '\n']
	#idx:    0    1    2       3            4          5          6          7        8
	
	psnr_y = float(interesting_line[4])
	bitrate = float(interesting_line[3])
	
	return psnr_y, bitrate, time
	

import os
import urllib.request, urllib.error, urllib.parse
#Função que permite baixar o HM
def DO_DOWNLOAD(codec_path):
	if(os.path.exists(codec_path)):
		#se a pasta já existe, apagar tudo
		os.system('rm -rf ' + codec_path)
	
	#faz download do libaom e coloca na pasta desejada
	git_command = 'git clone https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM ' + codec_path
	
	#caso deseja fazer downgrade...
	if DOWNGRADE_TO != '':
		git_command += ' && cd ' + codec_path + ' && git reset --hard ' + DOWNGRADE_TO
	
	#executa o git
	os.system(git_command)
	

#Função que compila o HM
#O código já adapta para possíveis versões diferentes de sistema operacional
def DO_COMPILE(os_version, codec_path):
	
	#O VTM cria uma pasta bin, logo, preciso criar outra
	codec_build = codec_path[:-1] + '_build/'
	
	
	#se precisar compilar o libaom, então COMPILA
	if(os.path.exists(codec_build)):
		#se a pasta já existe, apagar tudo pra deixar uma compilação limpa
		os.system('rm -rf ' + codec_build)
		os.system('rm -rf ' + codec_path)
	os.system('mkdir ' + codec_build)
	
	cmake_command = 'cd ' + codec_build + ' && cmake -DCMAKE_BUILD_TYPE=Release ..'
	make_command = 'cd ' + codec_build + ' && make'
	
	os.system(cmake_command)
	os.system(make_command)
	
