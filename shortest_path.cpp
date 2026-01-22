#include<iostream>
#include<vector>
#include<climits>
using namespace std;

int num_towns,num_paths;
vector<vector<pair<int,int>>> adj = vector<vector<pair<int,int>>>(300);

vector<int> best_path;
int best_dist = -1;

void shortest_path(int start,int next,int dist,vector<int> path, vector<bool> visited){
    
    path.push_back(next);
    visited[next] = true;
    if(next==num_towns){

        if(dist<best_dist or best_dist==-1){
            best_dist = dist;
            best_path = path;
        }
        return;
    }
    if (adj[next].size()==0) return;

    for(auto& p: adj[next]){
        int new_next = p.first;
        int new_dist = dist + p.second;
        if (new_dist>=best_dist and best_dist!=-1) continue;
        if (visited[new_next]) continue;
        shortest_path(next,new_next,new_dist,path,visited);
    }
    return ;
}

int main(){
    cin>>num_towns>>num_paths;
    for(int i=0;i<num_paths;i++){
        int u,v,dist;
        cin>>u>>v>>dist;
        adj[u].push_back({v,dist});
    }

    for(auto& p: adj[1]){
        vector<int> path = {1};
        vector<bool> visited(num_towns+1,false);
        visited[1] = true;
        shortest_path(1,p.first,p.second,path,visited);
        
    }
    
    if (best_dist == -1){
        cout << -1 << endl;
        return 0;
    }
    for(int town: best_path){
        cout << town << " ";
    }
    cout<<endl;
    cout << best_dist << endl;
    
}