# Size of latent vector to generator
z_dim = 100
learning_rate_D =  .00005 # Thanks to Alexia Jolicoeur Martineau https://ajolicoeur.wordpress.com/cats/
learning_rate_G = 2e-4 # Thanks to Alexia Jolicoeur Martineau https://ajolicoeur.wordpress.com/cats/
batch_size = 32
epochs = 500
#epochs = 1
alpha = 0.2
beta1 = 0.5
from_checkpoint = True
data_resized_dir="../gan_data/128x128x3"