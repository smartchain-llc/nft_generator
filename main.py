from lib.Generator import Generator
from multiprocessing import Process

def split_nfts_for_processes(nfts = [], processor_count = 1):
    total_nfts = len(nfts)
    segment_count = 0
    number_of_nfts_per_segment = 0
    segmented_nfts = []

    if total_nfts % processor_count != 0:

        return 0
    else:
        number_of_nfts_per_segment = total_nfts / processor_count
        for i in range(0, processor_count):
            segmented_nfts.append(nfts[i * number_of_nfts_per_segment : ((i+1) * number_of_nfts_per_segment) - 1])
        return 1

def setup_processes(nft_groups = []):
    return 1

def join(processes = []):
    for i in range(0, len(processes)):
        processes[i].join()

def start(processes = []):
    for i in range(0, len(processes)):
        processes[i].start()

def process_nfts(nfts):
    for nft in nfts:
        nft.populate_imgs()
        nft.generate_image()
        nft.generate_metadata()

G = Generator()

G.parse_permutations()
# G.run()

thread_count = 3
processes = []
for i in range(0,thread_count):
    processes.append(Process(target = process_nfts, args=nfts[i]))
    processes[i].start()


for nft in G.nfts:
    # nft.populate_imgs()
    # nft.generate_image()
    nft.generate_metadata()

