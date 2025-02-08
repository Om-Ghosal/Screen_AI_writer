import torch # might want to use pytorch for cuda or it might give an error
import transformers
from transformers.utils import is_flash_attn_2_available
from transformers import pipeline

def s2t(filename):
    pipe = pipeline(
        "automatic-speech-recognition",
        model = "openai/whisper-large-v3",
        torch_dtype = torch.float16,
        device = "cuda:0",
        model_kwargs = {"attn_implementaion":"flash_attention_2"} if  is_flash_attn_2_available() else {
            "attn_implementation":"sdpa",
        },
    )

    outputs = pipe(
        filename,
        chunk_length_s=30,
        batch_size=24,
        return_timestamps=True,
        
    )

    return outputs['text']

if __name__ == "__main__":
    s2t("London has a diverse.wav")
