Get-ChildItem "D:\Documentos\Escuela\CC3002 - Metodologías de Diseño y Programación\Tareas\Marco y Luis\Tarea 2 - 2021 Primavera\aalistos" | ForEach-Object {
  if (Test-Path -Path $_ -PathType Container) {
    Write-Output "$($_.FullName)\Rubrica_T2.xlsx"
    py .\main.py "$($_.FullName)\Rubrica_T2.xlsx"
  }
}