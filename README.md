# SMARTCHAIN NFT Generator
Dynamically generate NFTs from different collections

## Dependencies
1. Pillow - [Documentation](https://pillow.readthedocs.io/en/stable/)
2. Python >= 3.9
## Setup

### Asset Layers and Base Image
The default configuration of this software requires that all layers to be permutated be placed in `assets/layers/<layer_name>/<layers>.png` and the base image to be placed in `assets/base/<base_name>/<base_img>.png`.

---

## Running the Software
The utility libraries will parse the information in both the `assets/layers/` & `assets/base/` directories to determine generation of *all* permutations. The permutations are stored in the Generator object's `nft` list.

When the Generators `run()` function is called, select the order in which the layers are pasted then select the position to paste the base image.

### Generation Order 
```
1. background 
2. outfit
3. hats
4. items
5. eyes
Select generation layer order: 1
1. outfit
2. hats
3. items
4. eyes
Select generation layer order: 

...

```

### Base Order Selection
```
1. background 
2. outfit
3. hats
4. items
5. eyes
Select the layer to insert base: 
```
The layer selected to be pasted *after* the base image. For example, to paste the base image between ```background``` and ```outfit``` select **2**

Assets folder is removed because it's secret for now