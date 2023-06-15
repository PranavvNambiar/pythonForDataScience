import urllib.request
import numpy as np

# We will need to re-retrieve the raw file, everytime we work with this as the token expires
# URL for the climate text file for the retrive file: https://jovian.com/abhisheknarayan73/jovian-tut3/v/17/files?filename=climate.txt
urllib.request.urlretrieve(
    "https://storage.googleapis.com/jvn/gists/abhisheknarayan73/2b747ac735a2493d9fef215372f128f0/raw/92b633d8d46142bda9f69bdfcbd485a5/climate.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=prod-proxy-user%40jovian.iam.gserviceaccount.com%2F20230615%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230615T183015Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=078d5af1feb23e0552f770feb5eccdc1f03826eb2d55a9813d13812cdbf3e634e19afe3450f55ed3a817fe59ec0f322f28deadc7693a1e90feeba49cf354d67f74afc740b55c6d61c2ddc01ed8cf22164d611524587ecfae417fb798ea1b8dbb0004d508a22f15244480be2793addb4fbfd2df8773cc6d3d4c8475f4847903510c3089662fb866df198816eba9c05210e4dedf9bf7b2360dcbc6a86aa05d2f9b89b66bc14db45923c642fdfdee2ecdf6f7b78154dd9c78922ae82f89e37694c351dc3264c12afb981d6e8324f827240a34c55dc75edb404f2e38dc6e8f13fd903f590d51129fad7274f080c99e6326388ad6e39f9970d0a7c7bce6a632bc10bd",
    "climate.txt",
)

# Delimiter is the seperator of the data in the CSV file
climate_data = np.genfromtxt("climate.txt", delimiter=",", skip_header=1)

print(climate_data)
print(climate_data.shape)

weights = np.array([0.3, 0.2, 0.5])

yields = climate_data @ weights

print(yields)
print(yields.shape)

# help(np.reshape)

climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)

print(climate_results)

np.savetxt(
    "climate_results.txt",
    climate_results,
    fmt="%.2f",
    header="temperature,rainfall,humidity,yield_apples",
    comments="COMMENT: This just puts a comment before the header in the saved txt file\n",
)
