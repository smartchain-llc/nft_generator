from concurrent.futures import thread
from lib.Generator import Generator
from multiprocessing import Process

def setup_processes(nft_groups = []):
    processes = []
    nfts = []
    for i in range(0,thread_count):
        processes.append(Process(target = process_nfts, args=(nft_groups[i], )))
        
    return processes

def join(processes = []):
    for i in range(0, len(processes)):
        processes[i].join()

def start(processes = []):
    for i in range(0, len(processes)):
        processes[i].start()

def process_nfts(nfts = list):
    for nft in nfts:
        nft.populate_imgs()
        nft.generate_image()
        nft.generate_metadata()

G = Generator()

G.parse_permutations()
G.run()
thread_count = 4
segmented_nfts = G.split_nfts_for_processes(thread_count)
processes = setup_processes(segmented_nfts)
start(processes)
join(processes)



