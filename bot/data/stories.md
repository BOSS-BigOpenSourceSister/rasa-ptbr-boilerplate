## story_login_form
* request_login
  - utter_login_form
  - login_form
  - form{"name": "login_form"}
  - form{"name": null}
* afirmar
  - utter_finaliza_forms

## story_login_form
* request_login
  - utter_login_form
  - login_form
  - form{"name": "login_form"}
* cancelar
  - utter_pergunta_cancelar
* negar
  - form{"name": "login_form"}
  - form{"name": null}
  - utter_finaliza_forms

## story_login_form_cancelar
* request_login
  - utter_login_form
  - login_form
  - form{"name": "login_form"}
* cancelar
  - utter_pergunta_cancelar
* afirmar
  - action_deactivate_form
  - form{"name": null}
  - utter_forms_cancelado
  - utter_continuar_conversa
* negar
  - utter_despedir

## story_login_form_cancelar
* request_login
  - utter_login_form
  - login_form
  - form{"name": "login_form"}
* cancelar
  - utter_pergunta_cancelar
* afirmar
  - action_deactivate_form
  - form{"name": null}
  - utter_forms_cancelado
  - utter_continuar_conversa

## testa acoes
* cumprimentar
    - utter_cumprimentar
* testa_acoes
    - action_teste

## testa acoes
* testa_acoes
    - action_teste

## testa slots
* informa_telefone
    - action_telefone

## path_religiao 1
* religiao
    - utter_religiao
    - utter_continuar_conversa

## path_religiao 2
* cumprimentar
    - utter_cumprimentar
* religiao
    - utter_religiao
    - utter_continuar_conversa

## path_time 1
* time
    - utter_time
    - utter_continuar_conversa

## path_time 2
* cumprimentar
    - utter_cumprimentar
* time
    - utter_time
    - utter_continuar_conversa

## path_genero 1
* genero
    - utter_genero
    - utter_continuar_conversa

## path_genero 2
* cumprimentar
    - utter_cumprimentar
* genero
    - utter_genero
    - utter_continuar_conversa

## path_star_wars 1
* star_wars
    - utter_star_wars
    - utter_continuar_conversa

## path_star_wars 2
* cumprimentar
    - utter_cumprimentar
* star_wars
    - utter_star_wars
    - utter_continuar_conversa

## path_piada 1
* piada
    - utter_piada
    - utter_continuar_conversa

## path_piada 2
* cumprimentar
    - utter_cumprimentar
* piada
    - utter_piada
    - utter_continuar_conversa

## path_license 1
* license
    - utter_license
    - utter_continuar_conversa

## path_license 2
* cumprimentar
    - utter_cumprimentar
* license
    - utter_license
    - utter_continuar_conversa

## path_onde_voce_mora 1
* onde_voce_mora
    - utter_onde_voce_mora
    - utter_continuar_conversa

## path_onde_voce_mora 2
* cumprimentar
    - utter_cumprimentar
* onde_voce_mora
    - utter_onde_voce_mora
    - utter_continuar_conversa

## path_como_estou 1
* como_estou
    - utter_como_estou
    - utter_continuar_conversa

## path_como_estou 2
* cumprimentar
    - utter_cumprimentar
* como_estou
    - utter_como_estou
    - utter_continuar_conversa

## path_playlist 1
* playlist
    - utter_playlist
    - utter_continuar_conversa

## path_playlist 2
* cumprimentar
    - utter_cumprimentar
* playlist
    - utter_playlist
    - utter_continuar_conversa

## path_comida 1
* comida
    - utter_comida
    - utter_continuar_conversa

## path_comida 2
* cumprimentar
    - utter_cumprimentar
* comida
    - utter_comida
    - utter_continuar_conversa

## path_cor 1
* cor
    - utter_cor
    - utter_continuar_conversa

## path_cor 2
* cumprimentar
    - utter_cumprimentar
* cor
    - utter_cor
    - utter_continuar_conversa

## path_relacionamento
* relacionamento
    - utter_relacionamento
    - utter_continuar_conversa

## path_filhos 1
* filhos
    - utter_filhos
    - utter_continuar_conversa

## path_filhos 2
* cumprimentar
    - utter_cumprimentar
* filhos
    - utter_filhos
    - utter_continuar_conversa

## path_signo 1
* signo
    - utter_signo
    - utter_continuar_conversa

## path_signo 2
* cumprimentar
    - utter_cumprimentar
* signo
    - utter_signo
    - utter_continuar_conversa

## path_triste 1
* triste
    - utter_triste
    - utter_continuar_conversa

## path_triste 2
* cumprimentar
    - utter_cumprimentar
* triste
    - utter_triste
    - utter_continuar_conversa

## path_historia 1
* historia
    - utter_historia
    - utter_continuar_conversa

## path_historia 2
* cumprimentar
    - utter_cumprimentar
* historia
    - utter_historia
    - utter_continuar_conversa

## cumprimentar
* cumprimentar
    - utter_cumprimentar

## Despedir
* despedir
    - utter_despedir

## Tudo Bem Story
* tudo_bem
    - utter_tudo_bem

## Oi Tudo Bem Story 
* cumprimentar
    - utter_cumprimentar
* tudo_bem
    - utter_tudo_bem

## Nao entendi
* diga_mais
    - utter_diga_mais  

## fallback
* out_of_scope
    - utter_fallback

## negar sem contexto
* negar
    - utter_despedir

## elogios 1
* elogios
    - utter_elogios
    - utter_continuar_conversa

## elogios 2
* cumprimentar
    - utter_cumprimentar
* elogios
    - utter_elogios
    - utter_continuar_conversa

## meajuda 1
* o_que_sei_falar
    - utter_o_que_sei_falar

## meajuda 2
* cumprimentar
    - utter_cumprimentar
* o_que_sei_falar
    - utter_o_que_sei_falar

## objetivo
* objetivo
    - utter_objetivo

## path_daria
* cumprimentar
    - utter_cumprimentar
* daria
    - utter_daria
    - utter_continuar_conversa

## falar_de_anime
* anime
    - utter_anime

## recomendacao_anime
* tudo_bem
    - utter_tudo_bem
* anime
    - utter_anime
    - utter_recomenda_anime

## avatar
* avatar
    - utter_avatar
    - utter_continuar_conversa

## harry_potter
* harry_potter
    - utter_harry_potter

## friends
* friends
    - utter_friends

## cumprimentar_friends
* cumprimentar
    - utter_cumprimentar
* friends
    - utter_friends
    - utter_temporadas_friends

## falar_da_boss
* o_que_e_boss
    - utter_boss_apresenta
    - utter_talk_like_a_boss

## falar_da_boss_com_conversinha
* tudo_bem
    - utter_tudo_bem
* o_que_e_boss
    - utter_boss_apresenta

## story_limpar_slots
* limpar_slots
    - action_restart

## pedir_conselho
* cumprimentar
    - utter_cumprimentar
* pedir_conselho
    - action_pedir_conselho

## informar_nome
* cumprimentar
    - utter_cumprimentar
* informar_nome
    - utter_informar_nome

## casa_hogwarts
* cumprimentar
    - utter_cumprimentar
* casa_hogwarts
    - utter_chapeu_seletor
    - action_sorting_hat

## fato_sobre_gato
* fatos_sobre_gatos
    - utter_fato_sobre_gatos
    - action_cat_facts
