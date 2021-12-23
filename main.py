from lib.Generator import Generator

G = Generator()

G.run()

for nft in G.nfts:
    nft.populate_imgs()
    nft.generate_image()

