#!/usr/bin/env python3

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
#       Script desenvolvido por Alex Borges, amborges@inf.ufpel.edu.br.        #
#                  Grupo de Pesquisa Video Technology Research Group -- ViTech #
#                                     Universidade Federal de Pelotas -- UFPel #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# script de configuração compatível com o arquivo main.py versão 1.4           #
################################################################################
__COMPATIBLE_WITH_VERSION__ = 1.4


################################################################################
#                     ARQUIVO DE CONFIGURAÇÃO DEDICADO PARA O                  #
################################################################################
#                                                                              #
#                                                                              #
#                          #####  #        #  #####                            #
#                          #       #      #   #                                #
#                          ###      #    #    #                                #
#                          #         #  #     #                                #
#                          #####      ##      #####                            #
#                                                                              #
#                                                                              #
################################################################################


 
################################################################################
###                            Configurações Gerais                          ###
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -###
### Aqui tu prepara as condições das simulações que queres executar para os  ###
### teus experimentos. Apesar de estar preparado inicialmente para o AVS3,   ###
### com o software xeve, modificações para outros formatos é relativamente   ###
### simples. Basicamente é necessário modificar algumas pastas e nomes. Ao   ###
### longo deste arquivo, vou comentando algumas funcionalidades.             ###
################################################################################


#################################
## Ativação de Funcionalidades ##
#################################

#Precisa baixar o xeve?
DOWNLOAD = True

#Se precisar que o download do xeve seja regredido para alguma versão passada
#então modifique o texto abaixo para a versão requerida. Utilize somente os
#seis primeiros caracteres da versão, por exemplo 'cd2950'
DOWNGRADE_TO = '017d3c'

#Precisa compilar o xeve?
COMPILE  = True

#Quer realizar somente uma única simulação, para ver alguma coisa específica?
TESTE    = False

#É para executar de fato o experimento, com todas as simulações possíveis?
EXECUTE  = True

#É para calcular as métricas de codificação
METRICS = True

#É para gerar o gráfico da curva de BD-Rate?
PLOT = True

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
FTBE = 10

#Número máximo de núcleos que podem ser utilizados simultaneamente
#Em geral, se tu selecionou os cores disponíveis, é pq eles podem
#ser utilizados. Acaso tiveres alguma restrição, modificar aqui.
#O detalhe é que o computador não utilizará todos os núcleos
#anotados em ALLOWED_CORES
MAX_CORES = len(ALLOWED_CORES)

#nome do codificador. Se houver alguma mudança, mude aqui
CODEC_NAME = 'bin/xeveb_app'

#tipo de extensão do vídeo. PREFERENCIALMENTE Y4M.
#MAS caso tu preferir utilizar YUV, modifique a função GENERATE_COMMAND
#para incluir as informações de altura, largura, bit-depth, subsample e fps.
VIDEO_EXTENSION = '.yuv'


##########################
## Definição das Pastas ##
##########################

#caminho da pasta de compilação do xeve
#é de lá que ele vai compilar e manter os executáveis
#Caso houver mais de uma versão de xeve, ir adicionando as pastas
# >>>
#>>>  ATENÇÃO: Todas devem estar na mesma pasta atual do projeto!!!!  <<<
# >>>
CODEC_PATHS = ['xeve']



############################# [ [ [ A  T  E  N  Ç  Ã  O ] ] ] ########################################
#       Aqui se encontram funções que poderão sofrer mudanças. Deve-se alterar o que for preciso     #
#           para que a linha de comando seja adequada ao codificador que se está utilizando          #
######################################################################################################

#entradas vindas da classe LIST_OF_EXPERIMENTS, esses valores não são alteráveis.
#todos os valores são do tipo texto.
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
def GENERATE_COMMAND(cq, folder, video_path, codec_path, home_path, path_id, extra_param, width, height, subsample, bitdepth, num_frames, frames_per_unit, unit_size):
	#criando cada parte da linha de comando. Lembrar do espaçamento entre os parâmetros
	
	#comando completo
	#./xevee/build/linux/xeveenc --verbose 2 --signature 1 --speed_level 0 --wpp_threads 1 --frm_threads 1 --i_period 1 --frames {FPS} --width {WDT} --height {HGT} --input_bit_depth {BD} --fps_num 30 --fps_den 1 --rc_type 0 --qp 27 --input {VIDEO} -o coded_{VIDEO}.avs3
	#linha de comando retirada do artigo DOI: 10.1109/ICME51207.2021.9428331
	# Possivelmente reforçado por ftp://47.93.196.121, “AVS-3 software platform.”
	
	#nome da configuração extra_param, se existir
	ep_name = ''
	if extra_param != '':
		ep_name = "_set_" + extra_param.replace(' ', '').replace('-', '').replace('=', '')
	
	#definindo a pasta da saída dos resultados
	this_folder = home_path + '/' + folder + '/cq_' + cq + '/'
	
	#PARÂMETROS
	
	#definindo o caminho e nome do executável: ./xeveenc
	executable_param = codec_path + CODEC_NAME
	
	#definindo o arquivo de configuração principal:
	main_cfg_param = ' --config ' + home_path + '/CFG/EVC_cfg/encoder_randomaccess_baseline.cfg'
	main_cfg_param += ' --verbose 2'
	
	#definindo as informações do vídeo
	video_param  = ' --width ' + str(width) #width
	video_param += ' --height ' + str(height) #hight
	video_param += ' --hz ' + str( int( float(frames_per_unit) / float(unit_size) ) ) #fps
	video_param += ' --input_bit_depth ' + str(bitdepth) #bit depth
	video_param += ' --output_bit_depth ' + str(bitdepth) #bit depth
	
		
	#definindo o nível de quantização
	quant_param  = ' --op_qp ' + str(cq)
	
	#definindo o limite de frames a ser executado
	limit_param = ' --frames ' + str(num_frames)
	
	#Condições especiais de configuração do limite de quadros
	#Caso o usuário limitar algum valor, usar esse valor
	if(FTBE > 0):
		limit_param = ' --frames ' + str(FTBE)
			
	
	#definindo o caminho que será salvo o arquivo de vídeo codificado
	codfile_param = ' --output ' + this_folder + 'video/coded_' + path_id +  ep_name + '.evc'
	
	#definindo o caminho do vídeo de entrada
	rawvideo_param = ' --input ' + video_path

	#definindo o caminho do arquivo de log e o comando para forçar saída nesse arquivo
	output_filename = this_folder + 'log/out_' + path_id +  ep_name + '.log'
	logfile_param = ' > ' + output_filename + ' 2>&1'
	
	#Criando a linha de comando completa
	codec_command  = executable_param 
	codec_command += main_cfg_param 
	codec_command += video_param 
	codec_command += quant_param 
	codec_command += limit_param 
	codec_command += codfile_param 
	codec_command += rawvideo_param 
	codec_command += logfile_param
	
	#o & comercial no final serve para colocar o processo em segundo plano!
	codec_command += ' &'
	
	#retornando a linha de comando e o arquivo de saída
	return codec_command, output_filename


#A seguinte função lê o arquivo de log e retorna os três valores relevantes de cada arquivo
#entrada, o nome do arquivo que se deseja ler
#saída, o PSNR-Y, o bitrate e o tempo de execução. Todas do tipo float
def get_psnr_bitrate_time(from_file):
	#abro o arquivo obtido do xeve
	f = open(from_file)
	#preciso da última linha, mas tenho que passar por todo o arquivo
	#Os dados de bitrate e PSNR estão em algumas linhas antes do final do arquivo
	foundSummary = False
	interesting_line = 0
	
	for lst_line in f:
		if "Summary ========================================================================" in lst_line:
			foundSummary = True
		if foundSummary:
			interesting_line += 1
			#Somente na terceira linha após o summary é que 
			#os dados de bitrate e psnr estão posicionados
			if(interesting_line == 2):
				psnr_line = lst_line
			if(interesting_line == 8):
				bitrate_line = lst_line
			if(interesting_line == 10):
				time_line = lst_line
				foundSummary = False
		pass
	f.close()
	
	#Neste momento, eu tenho três variáveis de interesse
	#psnr_line
	#  PSNR Y(dB)       : 32.5561
	#bitrate_line
	#Bitrate                           = 578.0800 kbps
	#time_line
	#Total encoding time               = 3546.000 msec, 3.546 sec
	
	#Agora é só capturar cada dado de interesse
	
	psnr_line = psnr_line.split(' ')
	psnr_y = float(psnr_line[-1])
	
	bitrate_line = bitrate_line.split(' ')
	bitrate = float(bitrate_line[-2])
	
	time_line = time_line.split(' ')
	time = float(time_line[-2])

	return psnr_y, bitrate, time
	

import os
#Função que permite baixar o xeve
def DO_DOWNLOAD(codec_path):
	if(os.path.exists(codec_path)):
		#se a pasta já existe, apagar tudo
		os.system('rm -rf ' + codec_path)
	
	#faz download do libaom e coloca na pasta desejada
	git_command = 'git clone https://github.com/mpeg5/xeve ' + codec_path
	
	#caso deseja fazer downgrade...
	if DOWNGRADE_TO != '':
		git_command += ' && cd ' + codec_path + ' && git reset --hard ' + DOWNGRADE_TO
	
	#executa o git
	os.system(git_command)

#Função que compila o xevee
#O código já adapta para possíveis versões diferentes de sistema operacional
def DO_COMPILE(os_version, codec_path):
	#se precisar compilar o xevee, então COMPILA
	if(os.path.exists(codec_path)):
		#se a pasta já existe, apagar tudo pra deixar uma compilação limpa
		os.system('rm -rf ' + codec_path)
	os.system('mkdir ' + codec_path)
	
	cmake_command = 'cd ' + codec_path + ' && cmake -DSET_PROF=BASE ..'
	make_command = 'cd ' + codec_path + ' && make'
	os.system(cmake_command)
	os.system(make_command)
