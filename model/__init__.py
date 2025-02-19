# loaders and samplers
from model.Base.utils import get_hits_activation

# BasicGrooveTransformer imports
from model.Base.BasicGrooveTransformer import GrooveTransformer
from model.Base.BasicGrooveTransformer import GrooveTransformerEncoder


# VAE Imports
import model.VAE.shared_model_components as VAE_components
from model.VAE.MonotonicGrooveVAE import GrooveTransformerEncoderVAE
from model.VAE.Density1D import Density1D
from model.VAE.Density2D import Density2D
