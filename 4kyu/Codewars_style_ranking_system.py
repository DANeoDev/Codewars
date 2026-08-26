class User:
    total_progress_to_rank = {0:-8, 100:-7, 200:-6, 300:-5, 400:-4, 500:-3, 600:-2, 700:-1,
                             800:1, 900:2, 1000:3, 1100:4, 1200:5, 1300:6, 1400:7, 1500:8}
    ranks=[-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        
    def __init__(self):
        self.total_progress = 0
        self.rank=-8
        self.progress=0
        
    
    def update_rank(self):
        self.rank=self.total_progress_to_rank[min((self.total_progress//100)*100 , 1500)] #i could scrap the dict and simply refer to ranks:  self.rank = self.ranks[min(self.total_progress // 100, 15)]
        return self.rank
    def inc_progress(self, kata_rank):
        
        d=self.ranks.index(kata_rank)-self.ranks.index(self.rank)
        if d<-1:
            increase=0
        if d==-1:
            increase=1
        if d==0:
            increase=3
        if d>0:
            increase= d*d*10
        self.total_progress+=increase
        self.update_rank()
        self.update_progress()
    def update_progress(self):
        if self.rank ==8:
            self.progress=0
        else:
            self.progress=self.total_progress % 100
        
        
