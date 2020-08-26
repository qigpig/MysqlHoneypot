import evalServer
from webServer import app
from multiprocessing import Pool

def web_server():
    app.run()

def eval_server():
    evalServer.run()

if __name__ == '__main__':
    pool = Pool(2)
    pool.apply_async(web_server, args=())
    pool.apply_async(eval_server, args=())
    pool.close()
    pool.join()