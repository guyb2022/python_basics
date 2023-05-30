from PIL import Image, ImageFilter
import concurrent.futures
import time

img_names = [f'{i}.jpg' for i in range(1,31)]
size = (1200,1200)

def process_image(img_name):
    img = Image.open(f"photos/pics/{img_name}")
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'photos/processed/{img_name}')
    print(f'{img_name} was processed')

if __name__ == '__main__':

    ## Serial procedure
    t1 = time.perf_counter()

    for img_name in img_names:
        img = Image.open(f"photos/pics/{img_name}")
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size)
        img.save(f'photos/processed/{img_name}')
        print(f'{img_name} was processed')

    t2 = time.perf_counter()
    print(f"Finished serial in {round(t2-t1,3)} second's")

    t1 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executer:
        results = executer.map(process_image, img_names)
    t2 = time.perf_counter()
    print(f"Finished parallel in {round(t2-t1,3)} second's")