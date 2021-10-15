from sense_hat import SenseHat
import time

sense = SenseHat()

def round_coord(d):
    """
    pré:dictionnaire des positions non arrondies
    post:liste de 5 tuples contenant les coordonnées arrondies
    """
    for k,el in d.items():
        #parcours du dico(d)
        print(k, str(el))
        if len(str(d[k])) == 4:
                if str(d[k]) =="-1.0" or int(d[k])<0:
                    d[str(k)]=-1
                else:
                    d[str(k)]=0
        elif str(d[k]) =="0.0":
            d[str(k)]=0
        else:
            print(d)
            d[str(k)]=1
            #gestion des float positifs
                    
    return d

def get_orientation():
    """
    pré: rien
    post: liste des 5 positions
    """
    ml=[]
    #liste de mouvements
    
    for i in range(0,5):
        raw = sense.get_gyroscope_raw()
        #dictionnaire du mouvement
        time.sleep(2)
        x = raw['x']
        y = raw['y']
        z = raw['z']
        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)
        doc={'y':y,'x':x,'z':z}
        #mise en float
        """print("mouvement"+str(i+1)+"\n"+str((doc['x'],doc['y'],doc['z'])))"""
        raw=round_coord(doc)
        print (raw)
        #mise en int
        """print("\n"+"dico des arrondis"+str(raw))"""
        m=(raw['x'],raw['y'],raw['z'])
        ml.append(m)
        """print (ml)"""
        #mise en liste de tuple
    return ml

"""get_orientation()"""
	


