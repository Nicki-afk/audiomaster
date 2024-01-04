class GeneralAudioExtractor :
    
    def extract(self , link : str ) :
        pass

class TikTokAudioExtractor : 

    def __init__(self , link : str) -> None:
        self.__link = link



    @property
    def link(self) : 
        return self.__link    

    @link.setter    
    def link(self , link) :
        self.__link = link
          
    
    def get_audio(self) : 
        pass
    

    


class YoutubeAudioExtractor : 
    def __init__(self , link : str) -> None:
        self.__link = link

  
    @property
    def link(self) : 
        return self.__link    

    @link.setter    
    def link(self , link) :
        self.__link = link
          
    
    def get_audio() : 
        pass
    
    


class UserAudioExtractor : 
    def __init__(self , videofile ) -> None:
      self.__videofile = videofile

    @property
    def videofile(self) :
        return self.__videofile
    
    @videofile.setter
    def videofile(self , videofile) : 
        self.__videofile = videofile
    
    def get_audio(self) : 
        pass
           

    

