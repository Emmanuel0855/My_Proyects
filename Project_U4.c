/*Project Unit 4 Programming: Create an algorithm that optimally assigns resources (e.g., servers) to various projects
within a tech company.
Chong Santiago Hungman  Data 2A
02/08/2024*/

#include <stdio.h>

// Declaro mis funcones
void initializeResources(int resources[], int numResources);
void initializeProjects(int projects[], int numProjects);
void allocateResource(int resources[], int projects[], int allocations[], int numResources, int numProjects);
void printAllocations(int allocations[], int numResources);

int main() {
    int numResources, numProjects;
    
    // Solicito el número de recursos y de proyectos
    printf("Enter the number of resources: ");
    scanf("%d", &numResources);
    
    printf("Enter the number of projects: ");
    scanf("%d", &numProjects);
    
    // Inicio mi distribución de mis arreglos
    int resources[numResources];
    int projects[numProjects];
    int allocations[numResources];
    
    // Obtengo mis recursos y mi número de proyectos
    initializeResources(resources, numResources);
    initializeProjects(projects, numProjects);
    
    // Guardo mi número de proyectos
    allocateResource(resources, projects, allocations, numResources, numProjects);
    
    // Imprimo las asignaciones respectivas
    printAllocations(allocations, numResources);
    
    return 0;
}

void initializeResources(int resources[], int numResources) {
    for (int i = 0; i < numResources; i++) {
        resources[i] = 1; // 1 significa la cantidad mis recursos disponibles
    }
}

void initializeProjects(int projects[], int numProjects) {
    for (int i = 0; i < numProjects; i++) {
        projects[i] = 1; // 1 significa el resurso necesario para los proyectos
    }
}

void allocateResource(int resources[], int projects[], int allocations[], int numResources, int numProjects) {
    int projectIndex = 0;
    
    for (int i = 0; i < numResources; i++) {
        allocations[i] = -1; // -1 significa que el recurso que no está colocado
        
        if (resources[i] == 1) {
            if (projects[projectIndex] == 1) {
                allocations[i] = projectIndex; // Asignar recurso a proyecto
                projects[projectIndex] = 0; // El proyecto tiene el recurso
                
                // Mueve el siguiente proyecto
                projectIndex++;
                if (projectIndex >= numProjects) {
                    projectIndex = 0; // Regreso al primer proyecto
                }
            }
        }
    }
}

void printAllocations(int allocations[], int numResources) {
    printf("Resource Allocations:\n");
    for (int i = 0; i < numResources; i++) {
        if (allocations[i] != -1) {
            printf("Resource %d is allocated to Project %d\n", i, allocations[i]);
        } else {
            printf("Resource %d is not allocated\n", i);
        }
    }
}