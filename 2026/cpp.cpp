#include<iostream>
#include<vector>
#include<cstring>
 
#define endl "\n"
#define MAX 901
using namespace std;
 
int K, N, F;
int Friend_Num[MAX];
bool Friend[MAX][MAX];
vector<int> Answer;
bool Select[MAX];
bool Flag = false;
 
void Input()
{
    cin >> K >> N >> F;
    for (int i = 0; i < F; i++)
    {
        int a, b;
        cin >> a >> b;
        Friend[a][b] = true;
        Friend[b][a] = true;
 
        Friend_Num[a]++;
        Friend_Num[b]++;
    }
}
 
void Print()
{
    for (int i = 1; i <= N; i++)
    {
        if (Select[i] == true) cout << i << endl;
    }
}
 
bool CanSelect(int x)
{
    for (int i = 1; i <= N; i++)
    {
        if (Select[i] == true)
        {
            if (Friend[x][i] == false) return false;
        }
    }
    return true;
}
 
void DFS(int Cur, int Cnt)
{
    if (Flag == true) return;
    if (Cnt == K)
    {
        Print();
        Flag = true;
        return;
    }
 
    for (int i = Cur + 1; i <= N; i++)
    {
        if (Friend[Cur][i] == false) continue;
        if (CanSelect(i) == false) continue;
        Select[i] = true;
        DFS(i, Cnt + 1);
        Select[i] = false;
    }
}
 
void Solution()
{
    for (int i = 1; i <= N; i++)
    {
        if (Friend_Num[i] < K - 1) continue;
        if (Flag == true) break;
        
        Select[i] = true;
        DFS(i, 1);
        Select[i] = false;
    }
 
    if (Flag == false) cout << -1 << endl;
}
 
void Solve()
{
    Input();
    Solution();
}
 
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    freopen("random.txt", "r", stdin);
    Solve();
 
    return 0;
}