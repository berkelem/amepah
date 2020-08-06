def main():
    input_file = "/Users/Laptop-23950/projects/wisemapping/data/masks/stripe_mask.fits"
    mask_map = WISEMap(input_file, 3)
    mask_map.read_data()
    mask_map.rotate_map(old_coord="E", new_coord="G")
    mask_map.filename = mask_map.filename.replace(".fits", "_G.fits")
    mask_map.write_data()

if __name__ == "__main__":
    main()
