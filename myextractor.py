class GeneralAudioExtractor :
    
    def extract(self , link : str ) :
        pass

class TikTokAudioExtractor : 

    def __init__(self , link : str) -> None:
        self.__link = link

    def set_link(self , link : str) :    
        self.__link = link
    
    def get_link(self) -> str : 
        return self.__link
    
    def get_audio() : 
        pass
    

    


class YoutubeAudioExtractor : 
    def __init__(self , link : str) -> None:
        self.__link = link

    def set_link(self , link : str) :    
        self.__link = link
    
    def get_link(self) -> str : 
        return self.__link
    
    def get_audio() : 
        pass
    
    


class UserAudioExtractor : 
    def __init__(self , videofile ) -> None:
      self.__videofile = videofile

    def set_videofile(self , videofile) -> None : 
        self.__videofile = videofile

    def get_videofile(self)  : 
        return __videofile
    
    def get_audio() : 
        pass
           

    

