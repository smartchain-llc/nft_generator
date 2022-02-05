from lib.Generator import Generator

G = Generator()

G.parse_permutations()
# G.run()

for nft in G.nfts:
    # nft.populate_imgs()
    # nft.generate_image()
    nft.generate_metadata()

