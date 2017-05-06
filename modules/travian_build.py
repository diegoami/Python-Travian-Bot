import traceback
import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
import travian_login,  travian_effettuaraids , travian_risorse , travian_villaggi , travian_mercato , travian_party , travian_accademia , travian_mail 
import travian_priorita, travian_sposta, travian_mail
import logging

def do_build(villo):
    dictvills =  travian_villaggi.getvillaggi()
    try:
        travian_villaggi.vaiavillaggio(dictvills, villo)
        do_check_build(villo)
        buildasf = villo+"BUILD"
        if ((travian_mail.get_build() == 1) or (travian_mail.get_string(buildasf ) == 1)):
            logging.debug( "BUILD ATTIVO")
            strasf = villo+"EXCLUDE"
            if (travian_mail.get_string(strasf)== 1):
                logging.debug( "EXCLUDING "+strasf)
            else:
                buildnewasf = villo+"BUILD_NEW"

                travian_villaggi.vaiavillaggio(dictvills, villo)
                minimo_livello = travian_resdorf.build_random_resource()
                if ((travian_mail.get_string("BUILD_NEW") or (travian_mail.get_string(buildnewasf) == 1))):
                    if (minimo_livello > 0):
                        travian_villaggi.vaiavillaggio(dictvills, villo)

                        travian_edifici.build_missing_edifici(minimo_livello)
    except:
        logging.exception( "do_build FAILED")

                        
def do_check_build(villo):
    dictvills =  travian_villaggi.getvillaggi()
    try:
        building_links = travian_resdorf.get_all_reslinks()
        
        for building in building_links:
    
            href = building.href
            nome= building.nome
            strasf = villo+nome

            if (nome != ""):
                if (travian_mail.get_string(strasf)):
                    travian_func.build(href) 
        all_nome_edifici = travian_language.get_all_nome_edifici()
        for edificio in all_nome_edifici:
           
            if (travian_mail.get_string(villo+edificio)):
                travian_villaggi.vaiavillaggio(dictvills, villo)
        
                travian_func.build_edificio(edificio)
    except:
        logging.exception("do_check_build FAILED")

