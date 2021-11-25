#!/usr/bin/env python3

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
#	   Script desenvolvido por Alex Borges, amborges@inf.ufpel.edu.br.		   #
#				  Grupo de Pesquisa Video Technology Research Group -- ViTech  #
#									 Universidade Federal de Pelotas -- UFPel  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
#																			   #
#																			   #
#											Versão 1.4, 14 de setembro de 2021 #
################################################################################




################################################################################
###				Execução e Gerenciamento das Simulações				         ###
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -###
### Aqui neste script está toda a execução das simulações, tudo previamente  ###
### preparado para lidar com as configurações realizadas no arquivo		     ### 
### CONFIGURATIONS.py. A princípio, nenhuma modificação é requerida aqui.	 ###
### Eu suspeito ter conseguido realizar a generalização adequada. Claro, há  ###
### condições e especificações bem pontuais de experimentos desejados por	 ###
### alguns pesquisadores, que fazem com que esse script não funcione como	 ###
### desejável. Modificações são bem vindas.								     S###
################################################################################


__THIS_VERSION__ = 1.4


############################################
## Importações de bibliotecas necessárias ##
############################################

#pacotes básicos do S.O.
import os
import subprocess
from subprocess import PIPE
import sys

if not (sys.version_info.major == 3 and sys.version_info.minor >= 5):
	print("É necessário ter Python 3.5 or superior para utilizar este script!")
	print("Atualmente você está utilizando a versão {}.{}.".format(sys.version_info.major, sys.version_info.minor))
	sys.exit(1)

try:
	#importações de pacotes python
	##pacote para looping de tempo do script
	from time import sleep
	##pacote requerido pelo backup.json
	import json
	##pacote para compilação
	import platform
	import distro
	##pacote requerido para manutenção da fila
	import queue
	##pacotes gráficos
	import pandas as pd
	import seaborn as sns
	import matplotlib.pyplot as plt
	import numpy as np
	##pacote requerido pelo BD-rate
	import scipy.interpolate
except:
	#Atualização de pacotes python
	print("Atualizando o pip")
	subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
	print("pip atualizado")
	for package in ["pandas", "seaborn", "matplotlib", "numpy", "scipy", "queue", "json", "platform", "distro", "time"]:
		print("Tentando instalar o pacote ", package)
		try:
			subprocess.check_call([sys.executable, "-m", "pip", "install", package])
			print("Pacote ", package, " atualizado com sucesso!")
			
			##pacotes para compilação
			if package == "platform":
				import platform
			elif package == "distro":
				import distro
		except:
			print("Não foi possível atualizar o pacote ", package)

	#importações de pacotes python
	##pacote para looping de tempo do script
	from time import sleep
	##pacote requerido pelo backup.json
	import json
	##pacote requerido para manutenção da fila
	import queue
	##pacotes gráficos
	import pandas as pd
	import seaborn as sns
	import matplotlib.pyplot as plt
	import numpy as np
	##pacote requerido pelo BD-rate
	import scipy.interpolate

	
#Selecionar o arquivo de configuração desejado
#import CFG.CONFIGURATIONS_AV1  as CFG
#import CFG.CONFIGURATIONS_AVS3  as CFG
#import CFG.CONFIGURATIONS_EVC  as CFG
#import CFG.CONFIGURATIONS_H264 as CFG
import CFG.CONFIGURATIONS_HEVC as CFG
#import CFG.CONFIGURATIONS_VP9  as CFG
#import CFG.CONFIGURATIONS_VVC  as CFG


if CFG.__COMPATIBLE_WITH_VERSION__ != __THIS_VERSION__:
	print("O arquivo de configuração não é compatível com este gerenciador. Por favor, acesse o repositório oficial e atualize os arquivos!")

#Esse é o arquivo de vídeos
import CFG.VIDEOS_SEQUENCES as VIDEOS
#import CFG.VIDEOS_SEQUENCES_ALL as VIDEOS


#####################
## Definição Geral ##
#####################

#Em geral, todos os arquivos vão ser iniciados da pasta atual
#O código abaixo pega a localidade do arquivo main.py, e remove 
#o nome do arquivo python, sobrando apenas a pasta onde ele está
#sendo executado
HOME_PATH = '/'.join(os.path.realpath(__file__).split('/')[:-1])



#############
## Classes ##
#############


#classe experimento. Aqui eu armazeno todos os dados essenciais
#para possibilitar a criação de cada experimento. Aproveito a
#existência da classe para gerenciar a sua execução
class EXPERIMENT:
	#cada experimento vai receber uma lista
	def __init__(self, 
				 cq = '', 
				 resolution = '',
				 video = '',
				 width = '',
				 height = '',
				 subsample = '',
				 bitdepth = '',
				 num_frames = '',
				 frames_per_unit = '',
				 num_unit = '',
				 codec_folder = '', 
				 extra_param = '', 
				 is_there_many_set_of_experiments = False):
		
		if (cq == '' and
			resolution == '' and
			video == '' and
			width == '' and
			height == '' and
			subsample == '' and
			bitdepth == '' and
			num_frames == '' and
			frames_per_unit == '' and
			num_unit == '' and
			codec_folder == '' and
			extra_param == '' and
			is_there_many_set_of_experiments == False
		):
			self.cq = None
			self.video_name = None
			self.video_file = None
			self.executed = False
			self.finished = False
			self.many_experiments = None
			self.codec_folder = None
			self.extra_param = None
			self.height = None
			self.width = None
			self.bitdepth = None
			self.subsample = None
			self.num_frames = None
			self.frames_per_unit = None
			self.num_unit = None
			self.psnr_y = None
			self.bitrate = None
			self.time = None
			self.command = None
			self.outputlog = None
			self.terminal_command = None
		else:
		
			#valor do CQ do experimento
			self.cq = str(cq)
			#nome do vídeo/pasta do experimento
			self.video_name = video.replace(CFG.VIDEO_EXTENSION, '')
			#caminho completo do vídeo
			self.video_file = VIDEOS.VIDEOS_PATH[resolution] + video + CFG.VIDEO_EXTENSION
			#identificador se há vários conjuntos de experimentos
			self.many_experiments = is_there_many_set_of_experiments
			#nome da pasta principal do codificador utilizado
			self.codec_folder = codec_folder
			#configuração extra que foi incluida
			self.extra_param = extra_param
			#altura do vídeo
			self.height = height
			#largura do vídeo
			self.width = width
			#produndidade de bits do vídeo
			self.bitdepth = bitdepth
			#subamostragem do vídeo
			self.subsample = subsample
			#numero de quadros exitentes no vídeo
			self.num_frames = num_frames 
			#numero de frames por unidade de tempo
			self.frames_per_unit = frames_per_unit
			#tamanho da unidade de tempo
			self.num_unit = num_unit
			
			#quando finalizar, eu já posso capturar os dados para cálculos de BD-rate
			self.psnr_y = None
			self.bitrate = None
			self.time = None
			
			#Gero o caminho completo onde está o codificador
			codec_path = '/'.join([HOME_PATH, codec_folder, 'bin/'])
			codec_path = codec_path.replace('//', '/')
			
			#linha de comando que será aplicado ao experimento
			#e também é obtido o arquivo de log após o fim do experimento
			self.command, self.outputlog = CFG.GENERATE_COMMAND(self.cq,
																self.video_name,
																self.video_file,
																codec_path,
																HOME_PATH,
																self.codec_folder,
																self.extra_param,
																self.width,
																self.height,
																self.subsample,
																self.bitdepth,
																self.num_frames,
																self.frames_per_unit,
																self.num_unit)
			#texto de identificação do processo no terminal
			cmd = self.command.split(CFG.CODEC_NAME)[1]
			cmd = cmd.split(CFG.VIDEO_EXTENSION)[0]
			self.terminal_command = cmd
	
	def get_command_line(self):
		return self.terminal_command
		
	#nos backup da vida, preciso reinterpretar os dados json
	def update(self, data):
		self.__dict__.update(data)
		
	#Função que grava em um csv os dados que recebe
	def export(self):
		filename = self.video_name + '/summary_of_all_data.csv'
		csv = open(filename, 'a')
		if os.path.getsize(filename) == 0:
			csv.write("set, cq, psnr_y, bitrate, time\n")
		
		if (self.extra_param == ''):
			text_to_show = self.codec_folder + " under anchor"
		else:
			text_to_show = self.codec_folder + " under " + self.extra_param
		csv.write(text_to_show + "," + self.cq + "," + str(self.psnr_y) + "," + str(self.bitrate) + "," + str(self.time) + "\n")
		
		csv.close()


####################################################################

#classe que armazena os núcleos que serão utilizados durante a execução deste script
class CORE_CONTROL:
	def __init__(self):
		self.core_queue = queue.Queue()
		for i in range(len(CFG.ALLOWED_CORES)):
			self.core_queue.put(CFG.ALLOWED_CORES[i])
	
	#verifica se há núcleos livres
	def is_there_free_cores(self):
		return not self.core_queue.empty()
	
	#captura o núcleo que está livre para uso
	def get_core_idx(self):
		if not self.core_queue.empty():
			return self.core_queue.get()
		return None

	def free_core(self, idx):
		self.core_queue.put(idx)

####################################################################

#Classe que armazena os experimentos que serão utilizados durante a execução deste script
class EXPERIMENT_CONTROL:
	def __init__(self):
		self.experiment_queue = queue.Queue()
		
		if(self.load_backup()):
			printlog("Dados do backup foram recuperados com sucesso!")
		else:
			#coleciono todas as configurações possíveis
			extra_params = ['']
			extra_params = [*extra_params, *CFG.EXTRA_PARAMS]
			
			#identifico se há mais de um conjunto de experimentos
			more_than_one_set_of_experiments = len(extra_params) > 1
			
			#de cada vídeo e cada CQ e cada configuração extra, gero os experimentos
			for resolution, video, width, height, subsample, bitdepth, num_frames, frames_per_unit, num_unit in VIDEOS.VIDEOS_LIST:
				for cq in CFG.CQ_LIST:
					for extra_p in extra_params:
						for codec_path in CFG.CODEC_PATHS:
							exp = EXPERIMENT(cq,
											 resolution,
											 video,
											 width,
											 height,
											 subsample,
											 bitdepth,
											 num_frames,
											 frames_per_unit,
											 num_unit,
											 codec_path,
											 extra_p,
											 more_than_one_set_of_experiments)
						
							self.experiment_queue.put(exp)
	
	
	#verifica se há experimentos a serem executados
	def is_there_experiment_in_queue(self):
		return not self.experiment_queue.empty()
		
	#captura o núcleo que está livre para uso
	def get_experiment(self):
		if not self.experiment_queue.empty():
			return self.experiment_queue.get()
		return None
	
	#retorna o tamanho da fila
	def queue_size(self):
		return self.experiment_queue.qsize()
		
	#remove elementos da fila enquanto este for maior que o valor informado
	def drop_queue(self, number):
		while self.experiment_queue() > number:
			self.experiment_queue.get()
			
	#caso precisar devolver algum experimento para a fila de execução
	def give_back(self, exp):
		self.experiment_queue.put(exp)
	
	#carrega os dados salvos, caso houver algum arquivo de backup
	#caso sucesso, retornar verdadeiro
	def load_backup(self):
		if(os.path.exists('backup.json')):
			#Aqui eu uso 'r' pq só quero que haja leitura
			backup_file = open('backup.json', 'r')
			jsoned = json.load(backup_file)
			
			#Caso o backup esteja vazio, ignorar
			if (len(jsoned) == 0):
				backup_file.close()
				return False
			
			#lê cada linha do backup e criar um novo experimento na fila de execução
			elements_added = 0
			for exp_dict in jsoned:
				exp = EXPERIMENT()
				exp.update(exp_dict)
				self.experiment_queue.put(exp)
				elements_added = elements_added + 1

			backup_file.close()
			printlog("Recarregamento dos dados efetuada com sucesso")
			printlog("Foram recuperados " + str(elements_added) + " experimentos")
			return True
		return False
		
####################################################################

#Classe que gerenciará os experimentos para que sejam executadas nos núcleos corretos
class FIFO_CONTROL:
	def __init__(self):
		#fila de experimentos
		self.core_control = CORE_CONTROL()
		self.exp_control = EXPERIMENT_CONTROL()
		
		self.MAX_EXPERIMENTS = self.exp_control.queue_size()
		
		#é preciso saber quem está executando
		self.executing = []
		
	#Faz uma busca pelos núcleos e verifica se ele está livre ou não
	#recebe como entrada o número do core que se está observando
	def is_core_free(self, core):
		#no terminal eu digitaria
		#top -1 -b -n 1
		top = subprocess.Popen(['top', '-1', '-b', '-n 1'], stdout=subprocess.PIPE)
		#aqui estarão a lista de todos os processos que estão rodando no núcleo pesquisado
		lines = top.communicate()[0].decode("utf-8")
		lines = lines.split('\n')
		top.stdout.close()
		
		cpu_core = '%Cpu' + str(core)
		
		is_free = True
		
		for line in lines:
			if (cpu_core in line):
				#Devo ter algo assim
				#%Cpu0  :100.0 us,  0.0 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
				#O meu interesse é no primeiro número, preciso ver se ele está acima de 50%
				cpu_usage = float(line.split(':')[1].split('us')[0])
				if cpu_usage > 50.0:
					is_free =  False
			break
		
		return is_free
	
	
	#Faz uma busca pelos processos em execução e verifica se determinado experimento
	#ainda está ou não sendo executado.
	#recebe como entrada o parâmetro que foi submetido para execução e o número do core
	def exists_command_being_executed_on_core(self, exp, core):
		#no terminal eu digitaria:
		#ps -eo psr,cpu,cmd | grep -E  "^[[:space:]]+[[:space:]]+CORE"
		
		#Aqui eu pego a lista de processos que estão no core X
		regex = "^[[:space:]]+" + str(core)
		p1 = subprocess.Popen(['ps', '-eo', 'psr,cpu,cmd'], stdout=subprocess.PIPE)
		p2 = subprocess.Popen(['grep', '-E', r'{}'.format(regex)], stdin=p1.stdout, stdout=subprocess.PIPE)
		p1.stdout.close()
		
		#aqui estarão a lista de todos os processos que estão rodando no núcleo pesquisado
		lines = p2.communicate()[0].decode("utf-8")
		
		#Agora verifico se existe a linha de comando informada entre os processos buscados
		if(exp.get_command_line() in lines):
			return True
		else:
			return False
	
	#A função é bem similar ao de cima, só que eu olho para todos os núcleos
	#atrás de alguma função que tenha o nome do codificador que estou utilizando.
	#Essa função serve para manter esse script aguardando até o real fim de todas
	#as simulações, de forma a possibilitar a geração dos BD-rates.
	def is_there_any_experiment_in_execution(self):
		#no terminal eu digitaria:
		#ps -eo psr,cpu,cmd | grep CODEC"
		
		#Aqui eu pego a lista de processos que estão rodando
		p1 = subprocess.Popen(['ps', '-eo', 'psr,cpu,cmd'], stdout=subprocess.PIPE)
		p2 = subprocess.Popen(['grep', '-E', CFG.CODEC_NAME], stdin=p1.stdout, stdout=subprocess.PIPE)
		p1.stdout.close()
		
		#aqui estarão a lista de todos os processos que estão rodando no núcleo pesquisado
		lines = p2.communicate()[0].decode("utf-8")
		
		if len(lines) > 0:
			#ainda tem coisa rodando
			return True
		return False
	
	#Faço uma busca por todos os processos em execução, a fim de encontrar aqueles que já finalizaram
	def clean_executions(self):
		for exp, core in self.executing:
			#if ( not self.exists_command_being_executed_on_core(exp, core) ):
			if self.is_core_free(core):
				self.finishing_experiment(exp, core)
	
	#manda rodar um experimento com base em seu index
	def execute_experiment(self):
		
		#antes de iniciar, é bom dar uma limpa nos processos
		self.clean_executions()
		
		#SE houver comando a ser executado e SE houver núcleo livre, então
		if(self.core_control.is_there_free_cores()):
			if(self.exp_control.is_there_experiment_in_queue()):
				exp = self.exp_control.get_experiment()
				core_idx = self.core_control.get_core_idx()
				
				#caso for a primeira vez que o video vai ser codificado,
				#criar nova pasta
				if(not os.path.exists(exp.video_name)):
					os.system('mkdir ' + exp.video_name)
				#Para cada CQ que se vai usar, criar pasta, caso não existir
				for cq in CFG.CQ_LIST:
					if(not os.path.exists(exp.video_name + '/cq_' + str(cq))):
						os.system('mkdir ' + exp.video_name + '/cq_' + str(cq))
						os.system('mkdir ' + exp.video_name + '/cq_' + str(cq) + '/log')
						os.system('mkdir ' + exp.video_name + '/cq_' + str(cq) + '/video')
				
				full_command = 'taskset -c ' + str(core_idx) + ' ' + exp.command
				
				#executa o comando em modo terminal	
				subprocess.call(full_command, shell=True)
				
				#armazena quem está executando
				self.executing.append([exp, core_idx])
			else: #não há mais experimentos
				return False
		return True
					
	#quando um experimento finaliza, tirar ele da lista de "em execução"
	#além disso, obtenho os valores dos arquivos e salvo eles em um csv
	def finishing_experiment(self, exp, core):
		#removo da lista
		self.executing.remove([exp, core])
		
		#libero o núcleo
		self.core_control.free_core(core)
		
		#Adicionado um try para verificar se a busca ocorre como esperado.
		#Em caso negativo, manter os valores nulos para as variáveis
		#No futuro, corrigir esse procedimento
		try:
			exp.psnr_y, exp.bitrate, exp.time = CFG.get_psnr_bitrate_time(exp.outputlog)
		except:
			printlog("FALHA ao obter os dados do log para o arquivo " + exp.outputlog + ".")
		
		#exporta os dados finalizados para o arquivo CSV
		exp.export()
		
		self.save_backup()
		
	#função específica para treinos
	#elimina parte dos experimentos para deixar apenas
	#a quantidade informada pelo parâmetro
	def dropTo(self, untilNum):
		self.exp_control.drop_queue(untilNum)
		self.MAX_EXPERIMENTS = self.exp_control.queue_size()
		
	#função que exporta em linha de comando todos os experimentos
	def export_commands(self):
		max_exp = self.exp_control.queue_size()
		for i in range(max_exp):
			exp = self.exp_control.get_experiment()
			printlog(exp.command)
			self.exp_control.give_back(exp)
			
	#exporta a classe inteira para um arquivo de backup
	def save_backup(self):
		#antes de conseguir salvar, eu preciso obter os dados dos experimentos
		#que ainda não foram finalizados. Eles estão OU em execução
		#OU aguardando na fila. Portanto, preciso capturar eles

		#Experimentos em execução
		experiments_list = []
		for experiment, core_idx in self.executing:
			experiments_list.append(experiment)

		#Experimentos na fila
		#OBS: não consigo simplesmente pegar os experimentos da fila
		#preciso esvaziar a fila e depois preencher ela novamente
		copy_queue = queue.Queue()
		while not self.exp_control.experiment_queue.empty():
			exp = self.exp_control.experiment_queue.get()
			copy_queue.put(exp)
			experiments_list.append(exp)
	
		while not copy_queue.empty():
			self.exp_control.experiment_queue.put(copy_queue.get())
		
		#abre com 'w' pq quero sobreescrever o dado antigo
		backup_file = open('backup.json', 'w')
		jsoned = json.dumps(experiments_list, default=lambda o: o.__dict__)
		backup_file.write(jsoned)
		backup_file.close()
		printlog("Arquivo de backup finalizado")
		
	#Retorna o percentual de experimentos finalizados
	def get_percentage_of_experiments_completed(self):
		numerator = self.MAX_EXPERIMENTS - (self.exp_control.queue_size() + len(self.executing))
		percentage = (numerator / (self.MAX_EXPERIMENTS + 1) ) * 100
		return "{:.2f}".format(percentage)

						

####################################################################



####################
## Funções Gerais ##
####################


#  !!!! A seguinte função NÃO É MINHA !!!!
# Código original em https://github.com/shengbinmeng/Bjontegaard_metric/blob/master/bjontegaard_metric.py
#Recebe quatro vetores, e calcula a curva entre eles.
#Quando colocamos o piecewise=1, os valores de BD-rate retornam com maior confiança!
def BD_RATE(R1, PSNR1, R2, PSNR2, piecewise=0):
	lR1 = np.log(R1)
	lR2 = np.log(R2)

	# rate method
	p1 = np.polyfit(PSNR1, lR1, 3)
	p2 = np.polyfit(PSNR2, lR2, 3)

	# integration interval
	min_int = max(min(PSNR1), min(PSNR2))
	max_int = min(max(PSNR1), max(PSNR2))

	# find integral
	if piecewise == 0:
		p_int1 = np.polyint(p1)
		p_int2 = np.polyint(p2)

		int1 = np.polyval(p_int1, max_int) - np.polyval(p_int1, min_int)
		int2 = np.polyval(p_int2, max_int) - np.polyval(p_int2, min_int)
	else:
		lin = np.linspace(min_int, max_int, num=100, retstep=True)
		interval = lin[1]
		samples = lin[0]
		v1 = scipy.interpolate.pchip_interpolate(np.sort(PSNR1), lR1[np.argsort(PSNR1)], samples)
		v2 = scipy.interpolate.pchip_interpolate(np.sort(PSNR2), lR2[np.argsort(PSNR2)], samples)
		# Calculate the integral using the trapezoid method on the samples.
		int1 = np.trapz(v1, dx=interval)
		int2 = np.trapz(v2, dx=interval)

	# find avg diff
	avg_exp_diff = (int2-int1)/(max_int-min_int)
	avg_diff = (np.exp(avg_exp_diff)-1)*100
	return avg_diff


#Função que recebe uma pasta, calcula as métricas de transcodificação e grava um novo arquivo csv nessa pasta
def coding_metrics_of(path_file):
	
	if(not os.path.exists(path_file + '/summary_of_all_data.csv')):
		printlog("Não existe o CSV com os dados da codificação na pasta '" + path_file + "' para geração das métricas de codificação.")
		return None
	
	csv = pd.read_csv(path_file + '/summary_of_all_data.csv')
	df = pd.DataFrame(csv)
	df.sort_values(by=['set', ' cq'], inplace=True)

	if df.isnull().values.any():
		print("Nao é possível obter as métricas da pasta " + path_file)
		return
  
	original_set = CFG.CODEC_PATHS[0] + ' under anchor'

	df_list = []

	for key in df['set'].unique():
		if key == original_set:
			original = df[df['set'] == key].copy()
		else:
			df_copy = df[df['set'] == key].copy()
			df_list.append(df_copy)

	R1 = original[' bitrate'].values.tolist()
	P1 = original[' psnr_y'].values.tolist()
	T1 = original[' time'].values.tolist()

	metricas_list = []

	for df_case in df_list:
		try:
			R2 = df_case[' bitrate'].values.tolist()
			P2 = df_case[' psnr_y'].values.tolist()
			T2 = df_case[' time'].values.tolist()

			bdrate = BD_RATE(R1, P1, R2, P2)
			set_name = df_case['set'].unique()[0]
			time_compare = sum(T2) / sum(T1)

			metricas_list.append([set_name, bdrate, time_compare])
			
			if CFG.PLOT:
				plot_bdrate_curve(P1,
								  R1, 
								  P2, 
								  R2,
								  path_file,
								  set_name,
								  bdrate)
			
		except:
			printlog("Falha ao calcular as métricas de codificação na pasta '" + path + "'")
			return None

	df_metricas = pd.DataFrame(metricas_list, columns=['configuration name', 'bd-rate', 'time versus/time anchor'])

	df_metricas_file = path_file + '/coding_metrics.csv'
	df_metricas.to_csv(df_metricas_file, encoding='utf-8', index=False)



#Função que lê os dados de psnr e bitrate para gerar um gráfico com a curva bd-rate
#entradas:
#	 p_1, psnr âncora (dados do arquivo out.log)
#	 b_1, bitrate âncora (dados do arquivo out.log)
#	 p_2, psnr experimento (dados do arquivo out_set_EXPERIMENTO.log)
#	 p_2, bitrate experimento (dados do arquivo out_set_EXPERIMENTO.log)
def plot_bdrate_curve(p_1, b_1, p_2, b_2, video_folder, experiment_text, bdrate):
	#vou transformar os quatro vetores em dois DataFrames, 
	#só pra aproveitar um código que já tenho
	data1 = []
	data2 = []
	for i in range(len(p_1)):
		data1.append([b_1[i], p_1[i]])
		data2.append([b_2[i], p_2[i]])
	
	anchor = pd.DataFrame(data1, columns=['bitrate', 'psnr_y'])
	versus = pd.DataFrame(data2, columns=['bitrate', 'psnr_y'])
	
	#Preparo os dados para mostrar no gráfico
	
	#tamanho do grafico
	sns.set(rc={'figure.figsize':(15,10)})
	#tamanho da fonte
	sns.set(font_scale=2)
	
	#Mando plotar as linhas
	ax = sns.lineplot(data=anchor, 
					  x='bitrate', 
					  y='psnr_y', 
					  linewidth=2.5, 
					  marker='o', 
					  markersize=14)
	ax = sns.lineplot(data=versus, 
					  x='bitrate', 
					  y='psnr_y', 
					  linewidth=2.5, 
					  marker='s', 
					  markersize=14, 
					  ax=ax)
	
	#digo o texto dos eixos
	ax.set(xlabel="bitrate (bps)", 
		   ylabel = "PSNR-Y (dB)")
	
	#adiciono a legenda da imagem
	ax.legend(labels=['anchor configuration', 
					  experiment_text + ' configuration'], 
			  loc='lower right')
	
	#adicionando o valor do BD-rate no gráfico
	#CASO não quiser, só comentar a linha de baixo
	#posição: x = o menor bitrate; y = maior psnr
	ax.text(b_1[-1], 
			p_1[0], 
			"BD-rate {:.3f}%".format(bdrate), 
			fontsize=20, 
			verticalalignment='top')
	
	#mando mostrar a grade
	plt.grid(True)
	
	#salvando o gráfico
	plt.savefig(video_folder + '/bdrate_curve_' + experiment_text + '.png')
	
	#fechando o gráfico
	plt.clf()

#Solução que achei para que as saídas do script fiquem salvas em um arquivo de log
def printlog(text = "", end = "\n"):
	if CFG.VERBOSE:
		#Caso VERBOSE, mostrar no terminal do usuário
		#ou no arquivo nohup.out, caso tiver utilizado o nohup
		print(text, end=end)
	f = open("script_log.log", 'a')
	f.write(text + end)
	f.close()
	
	
################
## __MAIN__() ##
################

printlog("Script Gerenciador de Experimentos de Codificação.")
printlog("\t\tversão " + str(__THIS_VERSION__))
printlog()

#Variável de controle do tempo
__WAITING_TIME__ = 10

#########################################################
##				 baixa o software					##
#########################################################

if CFG.DOWNLOAD:
	#Esse comando só vai baixar uma única versão do codec
	codec_path = '/'.join([HOME_PATH, CFG.CODEC_PATHS[0], ''])
	CFG.DO_DOWNLOAD(codec_path)
	
	#Caso existir mais de uma pasta de codec, então finalizar
	#o código e avisar o usuário que ele deve tomar atitudes
	if(len(CFG.CODEC_PATHS) > 1):
		print("\n\nATENÇÃO\n\nCaro usuário, esse script só possibilita o download de apenas uma única cópia do codec. No entanto foi identificado a existência de ", len(CFG.CODEC_PATHS), " pastas diferentes. Portanto, pede-se que você realize as modificações necessárias nas outras pastas. Quando tudo estiver pronto, por favor, desabilite a opção 'DOWNLOAD' e reexecute o script.")
		#Encerrando a execução
		sys.exit()
	

#############################################################
##				  Compila o software					 ##
#############################################################

if CFG.COMPILE:
	#captura a versão do sistema operacional e envia.
	#Isso é importante pois pode haver condições diferentes
	#de compilação do programa a depender so sistema operacional
	try:
		#Para versões anteriores ao python3 3.8
		ubuntu_version = platform.dist()[1]
	except:
		#Para versões 3.8 ou superior do python3
		ubuntu_version = distro.linux_distribution()[1]
	
	#para cada pasta de codec, compilar
	for codec in CFG.CODEC_PATHS:
		codec_path = '/'.join([HOME_PATH, codec, 'bin/'])
		codec_path = codec_path.replace('//', '/')
		CFG.DO_COMPILE(float(ubuntu_version), codec_path)


###############################################################
##					 Executa um Teste					  ##
## O código abaixo gera todas as simulações e manda executar ##
## somente a primeira simulação dentre todas.				##
###############################################################


if CFG.TESTE:
	#crio o controlador de execução
	fifo_control = FIFO_CONTROL()
	
	#mostro quantas simulações são possíveis de serem realizadas
	printlog("Com a configuração estabelecida, há um total de " + 
			  str(fifo_control.MAX_EXPERIMENTS) + 
			  " simulações que podem ser realizadas.")
	
	fifo_control.execute_experiment()
	
	copy_of_exp = fifo_control.executing[0][0]
	copy_of_core = fifo_control.executing[0][1]
	
	printlog("A linha de comando que está sendo executada no CORE " + 
			 str(copy_of_core) +
			 " é: \n" +
			 copy_of_exp.command)
	
	while (fifo_control.is_there_any_experiment_in_execution()):
		printlog("\nEsperando Simulações em Andamento\n")
		sleep(__WAITING_TIME__)
	
	#é preciso se certificar que os núcleos estão limpos para possibilitar a geração das métricas
	fifo_control.finishing_experiment(copy_of_exp, copy_of_core)
	
	printlog("A simulação apresentou os seguintes dados:")
	printlog("PSNR-Y:" + str(copy_of_exp.psnr_y) + "dB")
	printlog("bitrate:" + str(copy_of_exp.bitrate) + "bps")
	printlog("tempo de execução:" + str(copy_of_exp.time) + "ms")
	


####################################################################
##				 Executa Todas as Simulações					##
## Aqui há a geração das simulações e gerenciamento das execuções ##
####################################################################

if CFG.EXECUTE:
	#crio o controlador de execução
	fifo_control = FIFO_CONTROL()

	#mostro quantas simulações são possíveis de serem realizadas
	printlog("Com a configuração estabelecida, há um total de " + 
			  str(fifo_control.MAX_EXPERIMENTS) + 
			  " simulações que podem ser realizadas.")


	#Executa todos os experimentos
	while ( fifo_control.execute_experiment() ):
		printlog("Aguarde. Já foram concluídos " + fifo_control.get_percentage_of_experiments_completed() + "% do experimento")
		sleep(__WAITING_TIME__)

	#Quando não houver mais nenhum na fila, só aguardar o fim
	while (fifo_control.is_there_any_experiment_in_execution()):
		printlog("Aguarde. Já foram concluídos " + fifo_control.get_percentage_of_experiments_completed() + "% do experimento")
		sleep(__WAITING_TIME__)
	
	#Para limpar de vez o arquivo de backup
	fifo_control.clean_executions()
	fifo_control.clean_executions()
	printlog("Aguarde. Já foram concluídos " + fifo_control.get_percentage_of_experiments_completed() + "% do experimento")

	printlog("\n\nFim das Simulações\n")
	
	
####################################################################
##				 Executa Todas as Simulações					##
## Aqui há a geração das simulações e gerenciamento das execuções ##
####################################################################

if CFG.METRICS:	
	for resolution, video, width, height, subsample, bitdepth, num_frames, frames_per_unit, num_unit in VIDEOS.VIDEOS_LIST:
		path = HOME_PATH + '/' + video
		coding_metrics_of(path)
		
	printlog("Geração das Métricas Finalizado!")
		
printlog("Script Gerenciador finalizado com sucesso!")
printlog("\n\nscript desevolvido por amborges@inf.ufpel.edu.br\n")
