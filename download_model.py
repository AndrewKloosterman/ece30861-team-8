from huggingface_hub import snapshot_download

def download_model(repo_id: str, local_dir: str = "./models") -> str:

    path = snapshot_download(
        repo_id = repo_id
        local_dir = local_dir
    )
    return path