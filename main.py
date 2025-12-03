%matplotlib widget

from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

sentences = [
    "I love pizza",
    "Italian pizzas are the best",
    "Tomato sauce is my favorite",
    "I love studying AI while eating pizza",
    "I am interested in art",
    "I love playing guitar",
    "My friends are the best",
    "Music helps me study",
    "To stay smart, we should study",
    "Neural networks are fascinating",
    "My friend's cat is black",
    "Birds singing is beautiful",
    "The weather is sunny",
    "Outside, the air is cold"
]

model = SentenceTransformer("all-MiniLM-L6-v2")


embeddings = model.encode(sentences)

pca = PCA(n_components=3)
embeddings_3d = pca.fit_transform(embeddings)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

for i, sentence in enumerate(sentences):
    x, y, z = embeddings_3d[i]
    ax.scatter(x, y, z)
    ax.text(x + 0.01, y + 0.01, z + 0.01, sentence, fontsize=8)

ax.set_title("3D Visualization of Sentence Embeddings")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")

plt.show()
