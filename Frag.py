
from requests.sessions import codes, default_headers
import telebot, requests, re, json

PRIVADO = [1702065456]
#
#
GRUPO = [-1001348184923,-1001616132625,-1001188581849,-1001507770035,-1001158279648,-1001503602761,-1001396629407,-1001456302751,-1001598127500,-1001429515931]
#
#
EXCEPT = []
#
#
ANONY = [] # OFF
bot = telebot.TeleBot("5666839145:AAF_-Fhyfns6bzWMkuiGcTolzFkYnGqBsz4")

description = "\n\nInformações By @zard_consultas_bot"

@bot.message_handler(commands=['cnpj'])
def zn(nome):
			id1 = nome.chat.id

			ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
			if id1 in ltnome:
				try:

					bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='HTML')
					msg = nome.text
					fl = msg.split('/cnpj')
					ip = re.sub('[^0-9]', '', msg)

					#response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>Informações By</b>: @zard_consultas_bot'

					response = 'Sem suporte para CPNJ'


					bot.send_chat_action(nome.chat.id, 'typing')
					bot.reply_to(nome, response, parse_mode='HTML')

				except Exception as e:
					print(e)
					bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
			else:
						bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏

☑️ 𝗠𝗘𝗡𝗨 𝗗𝗘 𝗖𝗢𝗠𝗔𝗡𝗗𝗢𝗦
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:

✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝙋𝙍𝙀𝙂𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝘼𝙄𝙇
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉

━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️

🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$8
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$15
• 1 MÊS = R$30

𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$15
• 31 𝘿𝙄𝘼𝙎 = R$30

━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊 💲

✅ 𝙋𝙞𝙭

<a href='http://t.me/ZardiNdu7'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')




@bot.message_handler(commands=['cpf'])
def zn(nome):
			id1 = nome.chat.id

			ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
			if id1 in ltnome:
				try:
					bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='HTML')
					msg = nome.text
					fl = msg.split('/cpf')
					ip = re.sub('[^0-9]', '', msg)
					response = requests.get(f'https://crew-apis-rest.tech/?token=f15507ddf0f05362a9c8fec3aaff9c521cb11f00&name=CpfHouse&documento={ip}')

					dados = {}

					text = response.json()

					if text.get('Status'):
						text = text.get('0')
						cadastro = text.get('cadastroCompleto')
						dados['CPF'] = ip
						dados['nome'] = cadastro.get('nome')
						dados['nome da mãe'] = cadastro.get('nomeMae')
						dados['nascimento'] = cadastro.get('dataNascimento')
						dados['origem'] = cadastro.get('regiaoOrigemCPF')
						dados['signo'] = cadastro.get('Escorpiao')

						dados['situação'] = cadastro.get('situacaoCPF')
						dados['ultima atualização'] = cadastro.get('dataAtualizacaoCPF')
						dados['sexo'] = cadastro.get('sexo')
						dados['RG'] = cadastro.get('rg')
						dados['titulo de eleitor'] = cadastro.get('tituloEleitor')
						dados['obito'] = cadastro.get('obito')
						dados['politicamente exposto'] = cadastro.get('pessoaPoliticamenteExposta')

						localizacao = text.get('localizacao')

						if localizacao:
							enderecos = localizacao.get('enderecos')

							if enderecos:
								dados['endereços'] = []

								for drop in enderecos:

									temp = {
										"cep": drop.get('cep'),
										"cidade": f"{drop.get('cidade')} - {drop.get('uf')}",
										"bairro": drop.get('bairro'),
										"logradouro": f"{drop.get('tipoLogradouro')} {drop.get('logradouro')}",
										"complemento": drop.get('complemento')
									}

									dados['endereços'].append(temp)


							telefones = localizacao.get('telefones')

							if telefones:
								dados['telefones'] = []

								for telefone in telefones:

									temp = {
										"DDD": telefone.get('ddd'),
										"número": telefone.get('numero'),
										"tipo": telefone.get('tipo')
									}

									dados['telefones'].append(temp)

							emails = localizacao.get('emails')

							if emails:
								dados['emails'] = emails

						qualificacao = text.get('qualificacao')

						pessoas = qualificacao.get('pessoasRelacionada')

						if pessoas:
							dados['pessoas'] = []
							for pessoa in pessoas:
								temp = {
									"cpf": str(pessoa.get('cpf')).replace('000',''),
									"nome": pessoa.get('nome'),
									"grau": pessoa.get('grauParentesco'),

								}

						text = ''
						for k, v in dados.items():

							if v != None:

								if type(v) == list:

									if len(v) >0:

										text += f"{k.upper()}\n"
										if type(v[0]) == dict:

											for item in v:

												for k2, v2 in item.items():
													if v2 != None:
														text += f"    {k2}: {v2}\n"

												text += f"\n"
											text += f"\n"


										else:
											for item in v:
												text += f"    {item}\n"

											text += f"\n"

								else:
									if v == False or v == 'N?o':
										v = 'Não'
									text += f"{k}: {v}\n\n"


					else:
						text = 'CPF não encontrado'

					#response = f'✔ <b>CPF LOCALIZADO</b> ✔\n\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>INFORMAÇÕES:</b>\n\n<b>• CPF</b>: <code>{req["cpf"]}</code>\n<b>• NOME</b>: <code>{req["nome"]}</code>\n<b>• DATA DE NASCIMENTO</b>: <code>{req["dtNascimento"]}</code>\n<b>• SEXO</b>: <code>{req["sexo"]}</code>\n<b>• SITUAÇÃO RECEITA FEDERAL</b>: <code>{req["situacao"]}</code>\n\n\n<b>• FAMILIARES</b>\n\n<b>• NOME DA MÃE</b>: <code>{req["mae"]}</code>\n\n\n<b>• ENDEREÇOS</b>\n\n<b>• RUA</b>: <code>{req["endereco"]}</code>\n<b>• NUMERO DA CASA</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• CIDADE</b>: <code>{req["cidade"]}</code>\n<b>• ESTADO</b>: <code>{req["estado"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>INFORMAÇÕES BY</b>: @zard_consultas_bot\n\n<b>Entre no meu grupo</b>: https://t.me/Zardconsultas'
					bot.send_chat_action(nome.chat.id, 'typing')
					bot.reply_to(nome, text, parse_mode='HTML')

				except Exception as e:
					print(e)
					bot.reply_to(nome, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='html')
			else:
						bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏

☑️ 𝗠𝗘𝗡𝗨 𝗗𝗘 𝗖𝗢𝗠𝗔𝗡𝗗𝗢𝗦
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:

✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝙋𝙍𝙀𝙂𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝘼𝙄𝙇
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉

━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️

🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$8
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$15
• 1 MÊS = R$30

𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$15
• 31 𝘿𝙄𝘼𝙎 = R$30

━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊 💲

✅ 𝙋𝙞𝙭

<a href='http://t.me/ZardiNdu7'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')




@bot.message_handler(commands=['cpf'])
def zn(nome):
			id1 = nome.chat.id

			ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
			if id1 in ltnome:
				try:
					bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='HTML')
					msg = nome.text
					fl = msg.split('/cpf')
					ip = re.sub('[^0-9]', '', msg)
					response = requests.get(f'https://crew-apis-rest.tech/?token=f15507ddf0f05362a9c8fec3aaff9c521cb11f00&name=CpfHouse&documento={ip}')

					dados = {}

					text = response.json()

					if text.get('Status'):
						text = text.get('0')
						cadastro = text.get('cadastroCompleto')
						dados['CPF'] = ip
						dados['nome'] = cadastro.get('nome')
						dados['nome da mãe'] = cadastro.get('nomeMae')
						dados['nascimento'] = cadastro.get('dataNascimento')
						dados['origem'] = cadastro.get('regiaoOrigemCPF')
						dados['signo'] = cadastro.get('Escorpiao')

						dados['situação'] = cadastro.get('situacaoCPF')
						dados['ultima atualização'] = cadastro.get('dataAtualizacaoCPF')
						dados['sexo'] = cadastro.get('sexo')
						dados['RG'] = cadastro.get('rg')
						dados['titulo de eleitor'] = cadastro.get('tituloEleitor')
						dados['obito'] = cadastro.get('obito')
						dados['politicamente exposto'] = cadastro.get('pessoaPoliticamenteExposta')

						localizacao = text.get('localizacao')

						if localizacao:
							enderecos = localizacao.get('enderecos')

							if enderecos:
								dados['endereços'] = []

								for drop in enderecos:

									temp = {
										"cep": drop.get('cep'),
										"cidade": f"{drop.get('cidade')} - {drop.get('uf')}",
										"bairro": drop.get('bairro'),
										"logradouro": f"{drop.get('tipoLogradouro')} {drop.get('logradouro')}",
										"complemento": drop.get('complemento')
									}

									dados['endereços'].append(temp)


							telefones = localizacao.get('telefones')

							if telefones:
								dados['telefones'] = []

								for telefone in telefones:

									temp = {
										"DDD": telefone.get('ddd'),
										"número": telefone.get('numero'),
										"tipo": telefone.get('tipo')
									}

									dados['telefones'].append(temp)

							emails = localizacao.get('emails')

							if emails:
								dados['emails'] = emails

						qualificacao = text.get('qualificacao')

						pessoas = qualificacao.get('pessoasRelacionada')

						if pessoas:
							dados['pessoas'] = []
							for pessoa in pessoas:
								temp = {
									"cpf": str(pessoa.get('cpf')).replace('000',''),
									"nome": pessoa.get('nome'),
									"grau": pessoa.get('grauParentesco'),

								}

						text = ''
						for k, v in dados.items():

							if v != None:

								if type(v) == list:

									if len(v) >0:

										text += f"{k.upper()}\n"
										if type(v[0]) == dict:

											for item in v:

												for k2, v2 in item.items():
													if v2 != None:
														text += f"    {k2}: {v2}\n"

												text += f"\n"
											text += f"\n"


										else:
											for item in v:
												text += f"    {item}\n"

											text += f"\n"

								else:
									if v == False or v == 'N?o':
										v = 'Não'
									text += f"{k}: {v}\n\n"


					else:
						text = 'CPF não encontrado'

					#response = f'✔ <b>CPF LOCALIZADO</b> ✔\n\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>INFORMAÇÕES:</b>\n\n<b>• CPF</b>: <code>{req["cpf"]}</code>\n<b>• NOME</b>: <code>{req["nome"]}</code>\n<b>• DATA DE NASCIMENTO</b>: <code>{req["dtNascimento"]}</code>\n<b>• SEXO</b>: <code>{req["sexo"]}</code>\n<b>• SITUAÇÃO RECEITA FEDERAL</b>: <code>{req["situacao"]}</code>\n\n\n<b>• FAMILIARES</b>\n\n<b>• NOME DA MÃE</b>: <code>{req["mae"]}</code>\n\n\n<b>• ENDEREÇOS</b>\n\n<b>• RUA</b>: <code>{req["endereco"]}</code>\n<b>• NUMERO DA CASA</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• CIDADE</b>: <code>{req["cidade"]}</code>\n<b>• ESTADO</b>: <code>{req["estado"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>INFORMAÇÕES BY</b>: @zard_consultas_bot\n\n<b>Entre no meu grupo</b>: https://t.me/Zardconsultas'
					bot.send_chat_action(nome.chat.id, 'typing')
					bot.reply_to(nome, text, parse_mode='HTML')

				except Exception as e:
					print(e)
					bot.reply_to(nome, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='html')
			else:
						bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏

☑️ 𝗠𝗘𝗡𝗨 𝗗𝗘 𝗖𝗢𝗠𝗔𝗡𝗗𝗢𝗦
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:

✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝙋𝙍𝙀𝙂𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝘼𝙄𝙇
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉

━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️

🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$8
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$15
• 1 MÊS = R$30

𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$15
• 31 𝘿𝙄𝘼𝙎 = R$30

━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊 💲

✅ 𝙋𝙞𝙭

<a href='http://t.me/ZardiNdu7'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')

@bot.message_handler(commands=['menu', 'help', 'start'])
def bniio(men):
	notbin = []
	bid = men.chat.id
	mensagem = men.text
	if men.text == '/menuu':
		bot.reply_to(men, '<b>' + '⚠ VOCÊ ESTÁ DIGITANDO ERRADO⚠' + '</b>')
	else:
		try:
			menu = f'Olá, <pre>{men.from_user.first_name} </pre><b>Veja meu menu</b>\n\n<b>━━━𝙈𝙚𝙣𝙪 Zard Consultas━━━</b>\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>Para consultar telefone você precisa digitar o Comando e em seguida digitar o DDD + NÚMERO.\nExemplo</b>: <code>/telefone 19996101067</code>\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>Para consultar os vizinhos você precisa digitar o comando e em seguida, digitar o cpf.\nExemplo</b>: <code>/vizinhos 27867260854</code>\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>Para consultar cnpj você precisa digitar o comando e em seguida, digitar o cnpj da empresa.\nExemplo</b>: <code>/cnpj 27865757000102</code>\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>Para consultar cpf você precisa digitar o comando e em seguida, digitar o cpf.\nExemplo</b>: <code>/cpf 00000000353</code>\n<b>━━━━━━━━━━━━━━━</b>\n<b>𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙘̧𝙤̃𝙚𝙨 𝙗𝙮:</b> @zard_consultas_bot'

			bot.reply_to(men, menu, parse_mode='HTML')
		except:
					bot.reply_to(men, 'VOCÊ ESTÁ DIGITANDO ERRADO',)

@bot.message_handler(commands=['vizinhos'])
def byti(men):
			chtid = men.chat.id
			permitidos = PRIVADO + GRUPO + EXCEPT + ANONY + [-1001414552721,-1001369485386]
			if int(chtid) in permitidos:
				if men.text == '/vizinhos':
					bot.reply_to(men, 'VIZINHOS Checker - Consulta de VIZINHOS, obtém os nomes dos vizinhos do portador do número de CPF.' + '\n\n' + 'Formato' + '\n' + '27867260854' + '\n' + 'ou' + '\n' + '278.672.608-54' + '\n\n' + '/vizinhos 27867260854')

				else:
					header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
							  'upgrade-insecure-requests': '1', 'save-data': 'on',
							  'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
							  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
							  'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
							  'sec-fetch-user': '?1',
							  'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
							  'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
							  'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
							  'cookie': '_ga=GA1.2.971515152.1596724424',
							  'cookie': '_gid=GA1.2.109978583.1596724424'}
					num = re.sub('[^0-9]', '', men.text)
					envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

					if "itemMoradores" in envia:
						try:
							bot.reply_to(men, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='html')

							viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
								   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
								   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
								   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

							bot.reply_to(men, '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' 'Informações By: @zard_consultas_bot' '</b>' , parse_mode='html')
						except:
							try:
								viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
									   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

								bot.reply_to(men,
											 '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙘̧𝙤̃𝙚𝙨 𝙗𝙮: @zard_consultas_bot' '</b>',
											 parse_mode='html')
							except:
								bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>', parse_mode='HTML')



					else:
						bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>️', parse_mode='html')

			else:
				bot.reply_to(men, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏

☑️ 𝗠𝗘𝗡𝗨 𝗗𝗘 𝗖𝗢𝗠𝗔𝗡𝗗𝗢𝗦
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:

✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝙋𝙍𝙀𝙂𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙀𝙈𝘼𝙄𝙇
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉

━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️

🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$8
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$15
• 1 MÊS = R$30

𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$15
• 31 𝘿𝙄𝘼𝙎 = R$30

━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊 💲

✅ 𝙋𝙞𝙭

<a href='http://t.me/ZardiNdu7'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')







@bot.message_handler(commands=['telefone'])
def zn(nome):
			id1 = nome.chat.id

			ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
			if id1 in ltnome:
				try:
					bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='HTML')
					msg = nome.text
					fl = msg.split('/telefone')
					ip = re.sub('[^0-9]', '', msg)
					url = requests.get('' + ip)
					req = url.json()
					req = f'✔ <b>Numero localizado</b> ✔\n\n<b>Informações:</b>\n\n<b>• TELEFONE</b>:\n <code>{req["TELEFONE"]}</code>\n<b>Informações By</b>: @zard_consultas_bot\n\n<b>Entre no meu grupo</b>: https://t.me/Zardconsultas'
					response = req + description
					bot.send_chat_action(nome.chat.id, 'typing')
					bot.reply_to(nome, response)

				except Exception as e:
					print(e)
					bot.reply_to(nome, '<b>TELEFONE NÃO ENCONTRADO</b>', parse_mode='html')
			else:
				  bot.reply_to(nome, '<b>VOCÊ NÃO TEM AUTORIZAÇÃO</b>', parse_mode='HTML')










bot.polling()