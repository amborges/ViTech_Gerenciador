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
#                         #   #   #####  #      #   #                          #
#                         #   #       #  #      #   #                          #
#                         #####   #####  #####  #####                          #
#                         #   #   #      #   #      #                          # 
#                         #   # # #####  #####      #                          #
#                                                                              #
#                                                                              #
################################################################################


 
################################################################################
###                            Configurações Gerais                          ###
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -###
### Aqui tu prepara as condições das simulações que queres executar para os  ###
### teus experimentos. Apesar de estar preparado inicialmente para o H.264,  ###
### com o software JM, modificações para outros codificadores é relativamente###
### simples. Basicamente é necessário modificar algumas pastas e nomes. Ao   ###
### longo deste arquivo, vou comentando algumas funcionalidades.             ###
################################################################################


#################################
## Ativação de Funcionalidades ##
#################################

#Precisa baixar o JM?
DOWNLOAD = True

#Se precisar que o download do HM seja regredido para alguma versão passada
#então modifique o texto abaixo para a versão requerida. Utilize somente os
#seis primeiros caracteres da versão, por exemplo 'jm15.0'
DOWNGRADE_TO = '' # a 'jm19.0' já é a ultima, não colocar pq dá problemas de download

#Precisa compilar o JM?
COMPILE  = True

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
CODEC_NAME = 'lencod.exe'

#O h.264 não oferece suporte para arquivos Y4M, portanto, deixar sempre YUV
VIDEO_EXTENSION = '.yuv'


##########################
## Definição das Pastas ##
##########################

#caminho da pasta de compilação do JM
#é de lá que ele vai compilar e manter os executáveis
#Caso houver mais de uma versão de JM, ir adicionando as pastas
# >>>
#>>>  ATENÇÃO: Todas devem estar na mesma pasta atual do projeto!!!!  <<<
# >>>
CODEC_PATHS = ['JM']



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
	#./lencod.exe -d encoder.cfg -p SourceWidth={WDT} -p SourceHeight={HGT} -p FrameRate={FPS} -p QPISlice={QP} -p QPPSlice={QP} -p OutputFile=coded_{VIDEO}.h264 -p InputFile={VIDEO}.yuv & -p SourceBitDepthLuma={BD} -p SourceBitDepthChroma={BD} -p OutputBitDepthLuma={BD} -p OutputBitDepthChroma={BD} 
	#SE 444: -p ProfileIDC=244
	#SE 1080: -p LevelIDC=50
	#SE 4K: -p LevelIDC=60
	
	#nome da configuração extra_param, se existir
	ep_name = ''
	if extra_param != '':
		ep_name = "_set_" + extra_param.replace(' ', '').replace('-', '').replace('=', '')
	
	#definindo a pasta da saída dos resultados
	this_folder = home_path + '/' + folder + '/cq_' + cq + '/'
	
	#PARÂMETROS
	
	#definindo em qual núcleo o experimento será executado
	taskset_param = 'cd ' + this_folder + 'log && '
	taskset_param += 'taskset -c ' + core + ' '
	
	#definindo o caminho e nome do executável: ./lencod.exe
	executable_param = codec_path + CODEC_NAME
	
	#definindo o arquivo de configuração principal: -d encoder.cfg
	main_cfg_param = ' -d ' + codec_path + 'encoder.cfg'
	
	#Condições especiais de configuração
	#Caso vídeo for UHD4K:
	if (height >= 2160):
		main_cfg_param += ' -p LevelIDC=60'
	#Caso vídeo for HD1080:
	elif (height >= 1080):
		main_cfg_param += ' -p LevelIDC=50'
	
	#definindo as informações do vídeo
	video_param  = ' -p SourceWidth=' + str(width) #width
	video_param += ' -p SourceHeight=' + str(height) #hight
	video_param += ' -p FrameRate={:.2f}'.format(float(frames_per_unit) / float(unit_size)) #fps
	video_param += ' -p SourceBitDepthLuma=' + str(bitdepth) #bit depth
	video_param += ' -p SourceBitDepthChroma=' + str(bitdepth) #bit depth
	video_param += ' -p OutputBitDepthLuma=' + str(bitdepth) #bit depth
	video_param += ' -p OutputBitDepthChroma=' + str(bitdepth) #bit depth
	
	#Condições especiais de configuração do vídeo
	#Caso o vídeo tiver subamostragem 444
	if (subsample == 444):
		video_param += ' -p ProfileIDC=244'
	
	
	#definindo o nível de quantização
	quant_param  = ' -p QPISlice=' + str(cq)
	quant_param += ' -p QPPSlice=' + str(cq)
	
	
	#definindo o limite de frames a ser executado
	limit_param = ' -p FramesToBeEncoded=' + str(num_frames)
	
	#Condições especiais de configuração do limite de quadros
	#Caso o usuário limitar algum valor, usar esse valor
	if(FTBE > 0):
		limit_param = ' -p FramesToBeEncoded=' + str(FTBE)
			
	
	#definindo o caminho que será salvo o arquivo de vídeo codificado
	codfile_param = ' -p OutputFile=' + this_folder + 'video/coded_' + path_id +  ep_name + '.h264'
	
	#definindo o caminho do vídeo de entrada
	rawvideo_param = ' -p InputFile=' + video_path

	#definindo o caminho do arquivo de log e o comando para forçar saída nesse arquivo
	output_filename = this_folder + 'log/out_' + path_id +  ep_name + '.log'
	logfile_param = ' > ' + output_filename + ' 2>&1'
	
		
	#O H.264 Gera uma série de arquivos extras, vamos definir aonde esses arquivos ficarão
	#para possibilitar remover eles depois
	toremove1 = this_folder + 'video/coded_' + path_id +  ep_name + '.yuv'
	toremove2 = this_folder + 'log/leakybucketparam.cfg'
	toremove3 = this_folder + 'log/stats.dat'
	toremove4 = this_folder + 'log/log.dat'
	toremove5 = this_folder + 'log/data.txt'
	toremove_param  = ' -p ReconFile=' + toremove1
	toremove_param += ' -p LeakyBucketParamFile=' + toremove2
	toremove_param += ' -p StatsFile=' + toremove3
	remove_params_files = ' && rm -f ' + toremove1 + ' ' + toremove2 + ' ' + toremove3 + ' ' + toremove4 + ' ' + toremove5
	
	
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
	
	time_line = ''
	psnr_line = ''
	bitrate_line = ''
	
	for lst_line in f:
		if "Average data all frames" in lst_line:
			foundSummary = True
		if foundSummary:
			interesting_line += 1
			#Somente na terceira linha após o summary é que 
			#os dados de bitrate e psnr estão posicionados
			if(interesting_line == 3):
				time_line = lst_line
			if(interesting_line == 6):
				psnr_line = lst_line
			if(interesting_line == 11):
				bitrate_line = lst_line
	f.close()
	
	#Neste momento, eu tenho três variáveis
	#time_line, cujos dados estão como
	# Total encoding time for the seq.  :   3.336 sec (1.50 fps)
	#psnr_line, cujos dados estão como
	# Y { PSNR (dB), cSNR (dB), MSE }   : {  41.827,  41.383,   4.72876 }
	#bitrate_line, cujos dados estão como
	# Bit rate (kbit/s)  @ 30.00 Hz     : 2932.80
	
	
	#Cada uma dessas variáveis vai passar pelo mesmo processo
	#1) primeiro crio um vetor com o texto
	#2) depois removo elementos vazios desse vetor
	#3) capturo o elemento que me interessa
	
	#1)
	time_line = time_line.split(' ')
	psnr_line = psnr_line.split(' ')
	bitrate_line = bitrate_line.split(' ')
	
	#2)
	time_line = list(filter(lambda a: len(a) > 0, time_line))
	psnr_line = list(filter(lambda a: len(a) > 0, psnr_line))
	bitrate_line = list(filter(lambda a: len(a) > 0, bitrate_line))
	
	#3)
	#time_line é ['Total', 'encoding', 'time', 'for', 'the', 'seq.', ':', '3.438', 'sec', '(1.45', 'fps)\n']
	#       idx:    0         1          2       3      4      5      6      7       8        9      10
	time = float(time_line[7])
	#psnr_line é ['Y', '{', 'PSNR', '(dB),', 'cSNR', '(dB),', 'MSE', '}', ':', '{', '41.827,', '41.383,', '4.72876', '}\n']
	#       idx:   0    1     2       3         4       5       6     7    8    9      10         11          12      13
	psnr_y = float(psnr_line[10][:-1]) #removo a vírgula que tem ali
	#bitrate_line é ['Bit', 'rate', '(kbit/s)', '@', '30.00', 'Hz', ':', '2932.80\n']
	#          idx:    0       1         2       3      4      5     6       7
	bitrate = float(bitrate_line[7][:-1]) # removo o \n
	
	return psnr_y, bitrate, time
	

import os
#Função que permite baixar o JM
def DO_DOWNLOAD(codec_path):
	if(os.path.exists(codec_path)):
		#se a pasta já existe, apagar tudo
		os.system('rm -rf ' + codec_path)
	
	#A ultima versão conhecida é essa
	JM_VERSION = 'jm19.0'
	url = 'http://iphome.hhi.de/suehring/tml/download/'
	
	#Caso o usuário quiser outra, então buscar de uma pasta diferente
	if DOWNGRADE_TO != '':
		JM_VERSION = DOWNGRADE_TO
		url += 'old_jm/'
	
	command_line = 'wget ' + url + JM_VERSION + '.zip'
	command_line += ' && unzip ' + JM_VERSION + '.zip'# -d ' + CODEC_PATHS[0]
	command_line += ' && rm -f '+ JM_VERSION + '.zip'
	
	#executa a linha de comando
	os.system(command_line)


#Função que compila o JM
#O código já adapta para possíveis versões diferentes de sistema operacional
def DO_COMPILE(os_version, codec_path):
	
	#OBSERVACAO:
	#o codec_path já existe, portanto só preciso realizar um clean

	if(os.path.exists(codec_path)):
		#se a pasta já existe, apagar tudo pra deixar uma compilação limpa
		os.system('make -C ' + codec_path + '../ clean')
	
	#Não sei se faz diferença, atualmente estou testando apenas no Ubuntu 18.04
	make_command = 'cd ' + codec_path + '../ && bash unixprep.sh'
	make_command += ' && make -C ' + codec_path + '../ all'
	
	os.system(make_command)
