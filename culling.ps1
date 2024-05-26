IF (pip show pipenv)
{
	Write-Host "pipenv found"
} ELSE {
	Write-Host "installing pipenv"
	pip install pipenv
}

IF (dir .venv -erroraction 'silentlycontinue')
{
	Write-Host "Virtual environment found."
} ELSE {
	Write-Host "Creating a virtual environment."
	python -m venv .venv
}

IF (pipenv run pip show torch torchvision pygetwindow pillow)
{
	Write-Host "Requirements found, continuing."
} ELSE {
	Write-Host "Downloading requirements, this may take some time and about 1.7gb in storage, you can delete the files later"
	pipenv sync
}

pipenv run python culling.py

$delete = Read-Host "Do you wish to delete the downloaded virtual environment? (yes/no) "
if ($delete -eq "yes")
{
	rm -r .venv
	Write-Host "Virtual environment deleted."
	pip uninstall pipenv -yq
	Write-Host "pipenv deleted."
}
